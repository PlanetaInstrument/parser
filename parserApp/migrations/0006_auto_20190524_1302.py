# Generated by Django 2.0.13 on 2019-05-24 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserApp', '0005_site_class_value_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='class_value_article',
            field=models.CharField(default='', max_length=200, verbose_name='Класс арктикля - значение'),
        ),
        migrations.AddField(
            model_name='site',
            name='class_value_back',
            field=models.CharField(default='', max_length=200, verbose_name='Класс назад - значение'),
        ),
        migrations.AddField(
            model_name='site',
            name='class_value_category',
            field=models.CharField(default='', max_length=200, verbose_name='Класс категории - значение'),
        ),
        migrations.AddField(
            model_name='site',
            name='class_value_description',
            field=models.CharField(default='', max_length=200, verbose_name='Класс описания - значение'),
        ),
        migrations.AddField(
            model_name='site',
            name='class_value_head',
            field=models.CharField(default='', max_length=200, verbose_name='Класс заголовка - значение'),
        ),
        migrations.AddField(
            model_name='site',
            name='class_value_link_product',
            field=models.CharField(default='', max_length=200, verbose_name='Класс ссылки на продукт - значение'),
        ),
        migrations.AddField(
            model_name='site',
            name='class_value_navigation',
            field=models.CharField(default='', max_length=200, verbose_name='Класс навигации - значение'),
        ),
        migrations.AddField(
            model_name='site',
            name='class_value_price',
            field=models.CharField(default='', max_length=200, verbose_name='Класс цены - значение'),
        ),
    ]
