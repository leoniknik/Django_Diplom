# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-09 22:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Diplom', '0002_auto_20170509_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='raspberry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Diplom.Raspberry'),
        ),
    ]