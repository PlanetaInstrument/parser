# Generated by Django 2.0.13 on 2019-05-25 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserApp', '0006_auto_20190524_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='link_first',
            field=models.CharField(default='', max_length=200, verbose_name='Ссылка на первую нужную страницу'),
        ),
    ]
