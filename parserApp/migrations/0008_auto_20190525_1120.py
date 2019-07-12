# Generated by Django 2.0.13 on 2019-05-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserApp', '0007_site_link_first'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='atr_article',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Атрибут арктикля'),
        ),
        migrations.AlterField(
            model_name='site',
            name='atr_back',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Атрибут назад'),
        ),
        migrations.AlterField(
            model_name='site',
            name='atr_category',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Атрибут категории'),
        ),
        migrations.AlterField(
            model_name='site',
            name='atr_description',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Атрибут описания'),
        ),
        migrations.AlterField(
            model_name='site',
            name='atr_head',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Атрибут заголовка'),
        ),
        migrations.AlterField(
            model_name='site',
            name='atr_link_product',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Атрибут ссылки на продукт'),
        ),
        migrations.AlterField(
            model_name='site',
            name='atr_navigation',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Атрибут навигации'),
        ),
        migrations.AlterField(
            model_name='site',
            name='atr_price',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Атрибут цены'),
        ),
        migrations.AlterField(
            model_name='site',
            name='atr_products',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Атрибут продукта'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_article',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс арктикля'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_back',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс назад'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_category',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс категории'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_description',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс описания'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_head',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс заголовка'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_link_product',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс ссылки на продукт'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_navigation',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс навигации'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_price',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс цены'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_products',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс продукта'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_value_article',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс арктикля - значение'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_value_back',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс назад - значение'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_value_category',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс категории - значение'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_value_description',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс описания - значение'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_value_head',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс заголовка - значение'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_value_link_product',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс ссылки на продукт - значение'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_value_navigation',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс навигации - значение'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_value_price',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс цены - значение'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_value_products',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс продукта - значение'),
        ),
        migrations.AlterField(
            model_name='site',
            name='link',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Ссылка на сайт'),
        ),
        migrations.AlterField(
            model_name='site',
            name='link_first',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Ссылка на первую нужную страницу'),
        ),
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='Название сайта'),
        ),
    ]
