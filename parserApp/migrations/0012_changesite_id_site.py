# Generated by Django 2.0.13 on 2019-05-29 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parserApp', '0011_auto_20190529_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='changesite',
            name='id_site',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='parserApp.Site', verbose_name='Сайт'),
        ),
    ]
