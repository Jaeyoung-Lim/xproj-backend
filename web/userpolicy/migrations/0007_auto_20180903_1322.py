# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-03 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpolicy', '0006_auto_20180823_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpolicy',
            name='guessing_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userpolicy',
            name='identify_done',
            field=models.BooleanField(default=False),
        ),
    ]
