# Generated by Django 2.0.13 on 2019-05-27 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parserApp', '0008_auto_20190525_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='parserresult',
            name='id_site',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='parserApp.Site', verbose_name='Сайт'),
        ),
    ]
