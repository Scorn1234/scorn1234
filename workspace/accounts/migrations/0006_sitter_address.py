# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20160522_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitter',
            name='address',
            field=models.CharField(default='서울 성북구 정릉로 77', max_length=100),
        ),
    ]