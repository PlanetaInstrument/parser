# Generated by Django 2.0.13 on 2019-05-22 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='atr_article',
            field=models.CharField(max_length=200, verbose_name='Атрибут арктикля'),
        ),
        migrations.AlterField(
            model_name='site',
            name='atr_back',
            field=models.CharField(max_length=200, verbose_name='Атрибут назад'),
        ),
        migrations.AlterField(
            model_name='site',
            name='atr_category',
            field=models.CharField(max_length=200, verbose_name='Атрибут категории'),
        ),
        migrations.AlterField(
            model_name='site',
            name='atr_description',
            field=models.CharField(max_length=200, verbose_name='Атрибут описания'),
        ),
        migrations.AlterField(
            model_name='site',
            name='atr_head',
            field=models.CharField(max_length=200, verbose_name='Атрибут заголовка'),
        ),
        migrations.AlterField(
            model_name='site',
            name='atr_navigation',
            field=models.CharField(max_length=200, verbose_name='Атрибут навигации'),
        ),
        migrations.AlterField(
            model_name='site',
            name='atr_price',
            field=models.CharField(max_length=200, verbose_name='Атрибут цены'),
        ),
        migrations.AlterField(
            model_name='site',
            name='atr_products',
            field=models.CharField(max_length=200, verbose_name='Атрибут продукта'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_article',
            field=models.CharField(max_length=200, verbose_name='Класс арктикля'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_back',
            field=models.CharField(max_length=200, verbose_name='Класс назад'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_category',
            field=models.CharField(max_length=200, verbose_name='Класс категории'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_description',
            field=models.CharField(max_length=200, verbose_name='Класс описания'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_head',
            field=models.CharField(max_length=200, verbose_name='Класс заголовка'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_navigation',
            field=models.CharField(max_length=200, verbose_name='Класс навигации'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_price',
            field=models.CharField(max_length=200, verbose_name='Класс цены'),
        ),
        migrations.AlterField(
            model_name='site',
            name='class_products',
            field=models.CharField(max_length=200, verbose_name='Класс продукта'),
        ),
        migrations.AlterField(
            model_name='site',
            name='link',
            field=models.CharField(max_length=200, verbose_name='Ссылка на сайт'),
        ),
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Название сайта'),
        ),
    ]
