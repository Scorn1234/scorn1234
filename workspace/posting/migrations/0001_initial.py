# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 12:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateField(default=datetime.datetime(2016, 5, 12, 12, 36, 39, 511835, tzinfo=utc))),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Sitter')),
            ],
        ),
    ]
