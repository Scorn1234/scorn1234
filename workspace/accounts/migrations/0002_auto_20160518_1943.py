# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitter',
            name='number_of_pet_own',
        ),
        migrations.AddField(
            model_name='sitter',
            name='phoneNumber',
            field=models.CharField(default='01084332362', max_length=12),
        ),
    ]