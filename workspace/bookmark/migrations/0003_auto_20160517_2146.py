# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 12:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_auto_20160512_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 12, 46, 23, 648198, tzinfo=utc)),
        ),
    ]
