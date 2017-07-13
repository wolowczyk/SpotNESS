# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point', '0005_auto_20170712_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='location',
        ),
        migrations.AddField(
            model_name='point',
            name='lat',
            field=models.CharField(default='brak', max_length=81),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='point',
            name='lng',
            field=models.CharField(default='brak', max_length=81),
            preserve_default=False,
        ),
    ]
