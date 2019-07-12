# Generated by Django 2.0.13 on 2019-05-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('link', models.TextField()),
                ('atr_products', models.TextField()),
                ('class_products', models.TextField()),
                ('atr_category', models.TextField()),
                ('class_category', models.TextField()),
                ('atr_head', models.TextField()),
                ('class_head', models.TextField()),
                ('atr_article', models.TextField()),
                ('class_article', models.TextField()),
                ('atr_description', models.TextField()),
                ('class_description', models.TextField()),
                ('atr_price', models.TextField()),
                ('class_price', models.TextField()),
                ('atr_navigation', models.TextField()),
                ('class_navigation', models.TextField()),
                ('atr_back', models.TextField()),
                ('class_back', models.TextField()),
            ],
        ),
    ]