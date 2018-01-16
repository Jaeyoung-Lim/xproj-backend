# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-16 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20171206_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('female', 'female'), ('male', 'male'), ('other', 'other'), ('unstated', 'rather not say')], default='', max_length=10, verbose_name='gender'),
        ),
    ]
