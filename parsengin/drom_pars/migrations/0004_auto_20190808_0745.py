# Generated by Django 2.2.4 on 2019-08-07 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drom_pars', '0003_auto_20190807_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parsingdb',
            name='info',
        ),
        migrations.RemoveField(
            model_name='parsingdb',
            name='price',
        ),
        migrations.RemoveField(
            model_name='parsingdb',
            name='title',
        ),
    ]