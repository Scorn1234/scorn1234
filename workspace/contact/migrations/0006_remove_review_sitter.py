# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 16:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20160517_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='sitter',
        ),
    ]