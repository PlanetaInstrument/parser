# Generated by Django 2.0.13 on 2019-05-29 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parserApp', '0012_changesite_id_site'),
    ]

    operations = [
        migrations.RenameField(
            model_name='changesite',
            old_name='id_site',
            new_name='id_changed_site',
        ),
    ]