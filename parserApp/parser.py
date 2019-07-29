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
    link_second = 'https://shop.dewalt.ru/elektroinstrument/dreli/bezudarnye-akkumulyatornye-dreli-shurupoverty-1.html'
    link_fourth = 'https://shop.dewalt.ru/elektroinstrument/shurupoverty/bezudarnye-akkumulyatornye-dreli-shurupoverty-2.html'
    link_fifth = 'https://shop.dewalt.ru/elektroinstrument/gaykoverty.html'

    atr_products = post.atr_products
    class_products = post.class_products
    class_value_products = post.class_value_products.replace('*', "")

    atr_category = post.atr_category
    class_category = post.class_category
    class_value_category = post.class_value_category.replace('*', "")

    atr_main_category = post.atr_main_category
    class_main_category = post.class_main_category
    class_value_main_category = post.class_value_main_category.replace('*', "")

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

    all_link = [link_first]
    start_links = [link_first]





    def get_html(url): # возвращает r.text любой ссылки
        r = requests.get(url)
        return r.text


    def make_all(url): # эта функция запускается потоком в main функции
        html = get_html(url) # главная категория
        get_link_category(html)
        data = get_page_data(html_product) # передаем параметром r.text страиницы с конкретным товаром


    def get_all_links(html, links):  # находит все ссылки с главными категориями
        soup = BeautifulSoup(html, 'lxml')
        href = soup.find_all(atr_main_category, attrs={class_main_category:class_value_main_category})
        for i in href:
          for link in i.find_all('a'):
            links += [link['href']]
        return links


    def get_link_category(html):
        soup = BeautifulSoup(html, 'lxml')
        def inspect(soup): # перебираем категории или переходим на страницу с товарами
            print (" ")
            print ("inspect")
            print (" ")
            if soup.find_all(atr_products, attrs={class_products:class_value_products}) == []: # товары
                if soup.find_all(atr_category, attrs={class_category:class_value_category}) == []: # подкатегории
                    if soup.find_all(atr_main_category, attrs={class_main_category:class_value_main_category}): # main категории
                        for i in soup.find_all(atr_main_category, attrs={class_main_category:class_value_main_category}):
                            links = i.find('a')
                            link_item = links.attrs['href']
                            if link_item in all_link: # если по этой ссылке уже переходили
                                print(link_item, "-----------------LINK_ITEM---------------")
                                continue
                            else:
                                source2 = requests.get(link+link_item).text
                                soup = BeautifulSoup(source2, 'lxml')  # soup - это ссылка на следующую страницу, возможно на страницу с товаром
                                all_link.append(link_item)
                                inspect(soup)
                    else:
                        print('------end parser------')
                        return 1
                else:
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

        def all_product(soup): # перебор по всем товарам на странице
            print (" ")
            print ("all_product")
            print (" ")
            for item in soup.find_all(atr_products, attrs={class_products:class_value_products}):  # for перебирает все товары на странице

                # находим ссылку для товара под индексом item (смотреть верхний for)
                links = item.find(atr_link_product, attrs={class_link_product:class_value_link_product}).a
                link_item = links.attrs['href']
                all_link.append(link_item)
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


    def get_page_data(html): # находим заголовок, артикль, описание, цену
        soup = BeautifulSoup(html, 'lxml')

        try:
            headline = soup.find(atr_head, attrs={class_head:class_value_head}).text
            print(headline)
        except Exception as e:
            headline = ''


        # article of item
        try:
            article = soup.find(atr_article, attrs={class_article:class_value_article}).text
            article = article.strip()
            article = article.replace(u'\xa0', ' ')
            article = article.split(' ', -1)[-1]
        except Exception as e:
            article = ''


        # description of item
        try:
            description = soup.find(atr_description, attrs={class_description:class_value_description}).text
        except Exception as e:
            description = ''

        # price of item
        try:
            price = soup.find(atr_price, attrs={class_price:class_value_price}).span.text
        except Exception as e:
            price = ''



        data = {'headline': headline, 'article': article, 'description': description, 'price':price}
        return data


    def write_db(data): # добавляем товары в базу данных
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


    url = link
    links = []
         #получение всех ссылок для парсинга с главной страницы
    all_links = get_all_links(get_html(url), links)
         #обеспечение многопоточности
         #функции смотри help
    max_threads = multiprocessing.cpu_count()
    p = multiprocessing.Pool(max_threads)

    results = p.map(make_all, all_links)


    for i in ParserResult.objects.filter(id_site=Site.objects.get(id = post.id)):
        n = i.article
        print(n, "n article -----------------------------------")
        orgs = TemporaryTable.objects.filter(article_product=n)
        if not orgs:
            print(orgs, 'orgs.article --------------------------')
            p = ParserResult.objects.get(article=n)
            print(p.article, 'p article s-----------------------')
            p.delete()
            print("DELETE --------------------")

        else:
            print(orgs, "orgs-----")
            print("good")

    TemporaryTable.objects.all().delete() # удаляется временная таблица

    print("-- THE END --")
