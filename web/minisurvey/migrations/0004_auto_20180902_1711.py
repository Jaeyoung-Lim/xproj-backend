# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-02 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minisurvey', '0003_minisurvey_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='minisurvey',
            name='article1_q1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='minisurvey',
            name='article1_q2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='minisurvey',
            name='article1_q3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='minisurvey',
            name='article2_q1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='minisurvey',
            name='article2_q2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='minisurvey',
            name='article2_q3',
            field=models.IntegerField(default=0),
        ),
    ]
