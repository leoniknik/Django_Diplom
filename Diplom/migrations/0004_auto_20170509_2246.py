# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-09 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diplom', '0003_auto_20170509_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raspberry',
            name='domain',
            field=models.CharField(default='', max_length=255, verbose_name='domain'),
        ),
        migrations.AlterField(
            model_name='raspberry',
            name='room',
            field=models.CharField(default='', max_length=255, verbose_name='room'),
        ),
    ]