import requests                   #выполняет HTTP-запросы
from bs4 import BeautifulSoup     #работа с HTML
import csv                        #работа с форматом данных CSV
from multiprocessing import Pool  #предоставляет возможность параллельных процессов
from . forms import ParserResultForm
from . models import Site, ParserResult, TemporaryTable, ChangeSite

def parser_site_new(post):
    link = post.link.replace('*', "")
    link_first = post.link_first
    link_second = 'https://metabo-shop.com.ua/index.php/cat/160'
    link_third = 'https://metabo-shop.com.ua/index.php/cat/160'
    link_fourth = 'https://metabo-shop.com.ua/index.php/cat/165'
    link_fifth = 'https://metabo-shop.com.ua/index.php/cat/162'

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

    all_link = [link_first, link_second, link_third, link_fourth]
    start_links = [link_first, link_second, link_third, link_fourth]

    def main():
        url = 'http://banknotes.finance.ua/'
        links = []
             #получение всех ссылок для парсинга с главной страницы
        all_links = get_all_links(get_html(url), links)
             #обеспечение многопоточности
             #функции смотри help
        with Pool(2) as p:
           p.map(make_all, all_links)

    if __name__ == '__main__':
        main()

    def get_html(url):
        r = requests.get(url)
        return r.text

    def make_all(url):
        html = get_html(url)
        data = get_page_data(html)
        write_csv(data)

    def get_all_links(html, links):
            #очистка содержимого файла - без его удаления
        f=open('coin.csv', 'w')
        f.close()
            #работа с html-кодом, задаются параметры блоков и адрес сайта
        soup = BeautifulSoup(html, 'lxml')
        href = soup.find_all('div', class_= "wm_countries")
        for i in href:
          for link in i.find_all('a'):
            links += [link['href']]
        return links

    def get_page_data(html):
        soup = BeautifulSoup(html, 'lxml')
        try:
            name = soup.find('div', 'pagehdr').find('h1').text
        except:
            name = ''
        try:
            massiv_price = [pn.find('b').text for pn in soup.find('div', class_ = 'wm_exchange').find_all('a', class_ = 'button', target = False)]+[pr.text for pr in soup.find('div', class_ = 'wm_exchange').find_all('td', class_ = 'amount')]
            if len(massiv_price)==6:   massiv_price=massiv_price[0]+massiv_price[3]+massiv_price[1]+massiv_price[4]+massiv_price[2]+massiv_price[5]
            elif  len(massiv_price)==4:
                 massiv_price=massiv_price[0]+massiv_price[2]+massiv_price[1]+massiv_price[3]
        except:
            massiv_price = ''
        data = {'name': name, 'price': massiv_price}
        return data

    def write_csv(data):
        with open('coin.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow( (data['name'], data['price']) )
