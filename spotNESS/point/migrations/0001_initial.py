# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        ('type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=27)),
                ('location', models.CharField(max_length=27)),
                ('description', models.TextField(null=True)),
                ('was_there', models.BooleanField()),
                ('photo', models.ImageField(upload_to='media', verbose_name='Photo')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(to='tag.Tag')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='type.SpotType')),
            ],
        ),
    ]
