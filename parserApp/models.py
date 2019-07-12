from django.db import models

class Site(models.Model):

    name = models.CharField(max_length=300, default='', blank=True, verbose_name=('Название сайта'),)
    link = models.CharField(max_length=200, default='', blank=True, verbose_name=('Ссылка на сайт'),)
    link_first = models.CharField(max_length=200, default='', blank=True, verbose_name=('Ссылка на первую нужную страницу'),)

    atr_products = models.CharField(max_length=200, default='', blank=True, verbose_name=('Атрибут продукта'),)
    class_products = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс продукта'),)
    class_value_products = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс продукта - значение'),)

    atr_link_product = models.CharField(max_length=200, default='', blank=True, verbose_name=('Атрибут ссылки на продукт'),)
    class_link_product = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс ссылки на продукт'),)
    class_value_link_product = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс ссылки на продукт - значение'),)

    atr_category = models.CharField(max_length=200, default='', blank=True, verbose_name=('Атрибут категории'),)
    class_category = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс категории'),)
    class_value_category = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс категории - значение'),)

    atr_head = models.CharField(max_length=200, default='', blank=True, verbose_name=('Атрибут заголовка'),)
    class_head = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс заголовка'),)
    class_value_head = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс заголовка - значение'),)

    atr_article = models.CharField(max_length=200, default='', blank=True, verbose_name=('Атрибут арктикля'),)
    class_article = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс арктикля'),)
    class_value_article = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс арктикля - значение'),)

    atr_description = models.CharField(max_length=200, default='', blank=True, verbose_name=('Атрибут описания'),)
    class_description = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс описания'),)
    class_value_description = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс описания - значение'),)

    atr_price = models.CharField(max_length=200, default='', blank=True, verbose_name=('Атрибут цены'),)
    class_price = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс цены'),)
    class_value_price = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс цены - значение'),)

    atr_navigation = models.CharField(max_length=200, default='', blank=True, verbose_name=('Атрибут навигации'),)
    class_navigation = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс навигации'),)
    class_value_navigation = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс навигации - значение'),)

    atr_back = models.CharField(max_length=200, default='', blank=True, verbose_name=('Атрибут назад'),)
    class_back = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс назад'),)
    class_value_back = models.CharField(max_length=200, default='', blank=True, verbose_name=('Класс назад - значение'),)


    def __str__(self):
        return self.name

class ParserResult(models.Model):
    id_site = models.ForeignKey('Site', default='', on_delete=models.CASCADE, verbose_name=('Сайт'),)
    headline = models.CharField(max_length=300, verbose_name=('Название'),)
    article = models.CharField(max_length=200, verbose_name=('Артикуль'),)
    description = models.TextField(verbose_name=('Описание'),)
    price = models.CharField(max_length=200, verbose_name=('Цена'),)
    link = models.CharField(max_length=200, verbose_name=('Ссылка'),)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=('Дата'),)

    def __str__(self):
        return '%s %s' % (self.id_site, self.headline)


class ChangeSite(models.Model):
    id_changed_site = models.ForeignKey('Site', default=1, null=True, blank=True, on_delete=models.CASCADE, verbose_name=('Сайт'),)
    id_product = models.CharField(max_length=200, verbose_name=('ID Товара'),)
    changed_field = models.CharField(max_length=200, verbose_name=('Поле изменения'),)
    old_value = models.TextField(verbose_name=('Старая информация'),)
    new_value = models.TextField(verbose_name=('Новая информация'), default='')
    article_change_product = models.CharField(max_length=200, verbose_name=('Артикуль изменения'), default='')

    def __str__(self):
        return '%s %s %s' % (self.id_product, self.changed_field, self.old_value)


class TemporaryTable(models.Model):
    article_product = models.CharField(max_length=200, verbose_name=('Артикуль временный'),)

    def __str__(self):
        return self.article_product
