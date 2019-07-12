#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing
import threading
import requests
import csv
import sqlite3
import re
import time
from . forms import ParserResultForm
from . models import Site, ParserResult, TemporaryTable, ChangeSite


def parser_site(post):

    link = post.link.replace('*', "")
    link_first = post.link_first
    link_second = '/catalog/sadovaya_tekhnika/'
    link_fourth = '/catalog/equipment_for_care_and_cleaning/'
    link_fifth = '/catalog/generatory/'

    atr_products = post.atr_products
    class_products = post.class_products
    class_value_products = post.class_value_products.replace('*', "")

    atr_category = post.atr_category
    class_category = post.class_category
    class_value_category = post.class_value_category.replace('*', "")

    atr_head = post.atr_head
    class_head = post.class_head
    class_value_head = post.class_value_head.replace('*', "")

    atr_article = post.atr_article
    class_article = post.class_article
    class_value_article = post.class_value_article.replace('*', "")

    atr_description = post.atr_description
    class_description = post.class_description
    class_value_description = post.class_value_description.replace('*', "")

    atr_price = post.atr_price
    class_price = post.class_price
    class_value_price = post.class_value_price.replace('*', "")

    atr_navigation = post.atr_navigation
    class_navigation = post.class_navigation
    class_value_navigation = post.class_value_navigation.replace('*', "")

    atr_back = post.atr_back
    class_back = post.class_back
    class_value_back = post.class_value_back.replace('*', "")

    atr_link_product = post.atr_link_product
    class_link_product = post.class_link_product
    class_value_link_product = post.class_value_link_product.replace('*', "")

    all_link = [link_first, link_second, link_fourth, link_fifth]
    start_links = [link_first, link_second, link_fourth, link_fifth]

    print("PEREMENNUE")

    def multi (l):
        print (" ")
        print ("multi")
        print (" ")
        source = requests.get(link+l).text
        soup = BeautifulSoup(source, 'lxml')   # soup - это ссылка на страницу с товарами

        inspect(soup)

    def inspect(soup):
        print (" ")
        print ("inspect")
        print (" ")
        if soup.find_all(atr_products, attrs={class_products:class_value_products}) == []:
            for item in soup.find_all(atr_category, attrs={class_category:class_value_category}):  # for перебирает все категории на странице

                # находим ссылку для следующей страницы
                links = item.find('a')
                link_item = links.attrs['href']
                if link_item in all_link: # если по этой ссылке уже переходили
                    continue
                else:
                    source2 = requests.get(link+link_item).text
                    soup = BeautifulSoup(source2, 'lxml')  # soup - это ссылка на следующую страницу, возможно на страницу с товаром
                    all_link.append(link_item)
                    inspect(soup)
        else:
            all_product(soup)

    def add_item_db(soup2, link_item):  # мы на странице конкретного товара, берем нужную инфу и заливаем в базу
        print (" ")
        print ("add_item_db")
        print (" ")
        try:
            headline = soup2.find(atr_head, attrs={class_head:class_value_head}).text
            print(headline)
        except Exception as e:
            headline = ''


        # article of item
        try:
            article = soup2.find(atr_article, attrs={class_article:class_value_article}).text
            article = article.strip()
            article = article.replace(u'\xa0', ' ')
            article = article.split(' ', -1)[-1]
            print ('article = ', article, '-------------split--------------------')
        except Exception as e:
            article = ''


        # description of item
        try:
            description = soup2.find(atr_description, attrs={class_description:class_value_description}).text
        except Exception as e:
            description = ''

        # price of item
        try:
            price = soup2.find(atr_price, attrs={class_price:class_value_price}).span.text
        except Exception as e:
            price = ''


        temporary = TemporaryTable(article_product=article) # временная таблица для отслеживания удалившихся товаров
        temporary.save()

        try: # если этот объект существует, проверяем изменения в полях
            obj = ParserResult.objects.get(id_site=Site.objects.get(id = post.id), article=article)
            print('TRY---', obj.headline)

            if (obj.headline != headline):
                change = ChangeSite(id_changed_site=Site.objects.get(id = post.id), id_product=obj.id, changed_field="Заголовок", old_value=obj.headline, new_value=headline, article_change_product=article)
                change.save()
                obj.headline = headline

            if (obj.description != description):
                print("DESCRIPTION !=  s-----------")
                change = ChangeSite(id_changed_site=Site.objects.get(id = post.id), id_product=obj.id, changed_field="Описание", old_value=obj.description, new_value=description, article_change_product=article)
                change.save()
                obj.description = description
                print("CHANGE DESCRIPTION -----------")

            if (obj.price != price):
                print(obj.price, obj.headline, obj.link, " ----- ", price, headline, link)
                change = ChangeSite(id_changed_site=Site.objects.get(id = post.id), id_product=obj.id, changed_field="Цена", old_value=obj.price, new_value=price, article_change_product=article)
                change.save()
                obj.price = price

            if (obj.link != link):
                change = ChangeSite(id_changed_site=Site.objects.get(id = post.id), id_product=obj.id, changed_field="Ссылка", old_value=obj.link, new_value=link, article_change_product=article)
                change.save()
                obj.link = link
            obj.save()
        except ParserResult.DoesNotExist: # если объекта не существует, создаем его
            obj = ParserResult(id_site=Site.objects.get(id = post.id), headline=headline, article=article, description=description, price=price, link=link)
            obj.save()
            print("EXCEPT---------")

    def all_product(soup):
        print (" ")
        print ("all_product")
        print (" ")
        for item in soup.find_all(atr_products, attrs={class_products:class_value_products}):  # for перебирает все товары на странице

            # находим ссылку для товара под индексом item (смотреть верхний for)
            links = item.find(atr_link_product, attrs={class_link_product:class_value_link_product}).a
            link_item = links.attrs['href']
            source2 = requests.get(link+link_item).text
            soup2 = BeautifulSoup(source2, 'lxml')  # soup - это ссылка на конкретный товар

            add_item_db(soup2, link_item)  # мы на странице конкретного товара, берем нужную инфу и заливаем в базу

        func_navigation(soup)

    def back_page(soup):   # функция переходит на предыдущую страницу в панели навигации по каталогу
        print (" ")
        print ("back_page")
        print (" ")
        for backs in soup.find_all(atr_back, attrs={class_back:class_value_back}):
            back = backs.find_all('a')[-1]
            back = back.attrs['href']
            source3 = requests.get(link+back).text
            soup = BeautifulSoup(source3, 'lxml')  # soup - это ссылка на предыдущую страницу в панели навигации, по каталогу
            inspect(soup)

    def func_navigation(soup): # если страниц с товаров больше 1, просматриваем все
        print (" ")
        print ("func_navigation")
        print (" ")
        if soup.find(atr_navigation, attrs={class_navigation:class_value_navigation}) == None:
            print("BACK_PAGE")
            back_page(soup)
        else:
            print ("NEXT_PAGE")
            navigation = soup.find_all(atr_navigation, attrs={class_navigation:class_value_navigation})[-1]
            source_name = navigation.attrs['href']
            source1 = requests.get(link+source_name).text
            soup = BeautifulSoup(source1, 'lxml')
            all_product(soup)


    # all_product(soup)

    # p1 = Process(target=multi, args=(link_first,))
    # p2 = Process(target=multi, args=(link_second,))
    # p1.start(); p2.start()
    # p1.join(); p2.join()


    # t1 = multiprocessing.Process(target=multi(link_first))
    # t2 = multiprocessing.Process(target=multi(link_second))
    # t1.start()
    # t2.start()



    for i in start_links:
        my_thread = threading.Thread(target=multi, args=(i,))
        print()
        print('THREAD ----------', i)
        print()
        my_thread.start()

    print()
    print("END for")
    print()

    # print("end parser--------------------------")
    # for i in ParserResult.objects.only("article"):
    #     print(i, "i -----------------------------------")
    #     n = i.article
    #     if n not in TemporaryTable.objects.only("article_product"):
    #         print(i.article, 'i.article --------------------------')
    #         p = ParserResult.objects.get(article=i.article)
    #         print(p, 'p -----------------------')
    #         p.delete()
    #         print("DELETE --------------------")
    # TemporaryTable.objects.all().delete() # удаляется временная таблица
