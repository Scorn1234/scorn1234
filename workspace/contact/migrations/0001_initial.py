# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 12:36
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('number_of_animal', models.IntegerField()),
                ('extra_request', models.CharField(max_length=300)),
                ('published_date', models.DateField(default=datetime.datetime(2016, 5, 12, 12, 36, 39, 517066, tzinfo=utc))),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Sitter')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=5)),
                ('comment', models.CharField(max_length=300)),
                ('published_date', models.DateField(default=datetime.datetime(2016, 5, 12, 12, 36, 39, 519393, tzinfo=utc))),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contact.Contact')),
                ('sitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Sitter')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='species_of_animal',
            field=models.ManyToManyField(db_table='동물 종류', to='contact.Species'),
        ),
    ]
