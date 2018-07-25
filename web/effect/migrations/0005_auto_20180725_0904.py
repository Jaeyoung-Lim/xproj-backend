# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-25 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('effect', '0004_effect_stakeholder_group'),
        ('userpolicy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='effect',
            name='user_policy',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='effects', to='userpolicy.UserPolicy'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='effect',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
