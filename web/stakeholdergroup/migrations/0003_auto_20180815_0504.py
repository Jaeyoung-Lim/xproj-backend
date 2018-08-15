# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-15 05:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stakeholdergroup', '0002_auto_20180807_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='stakeholdergroup',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stakeholder_group_custom', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stakeholdergroup',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
