# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20160517_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='published_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='review',
            name='published_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
