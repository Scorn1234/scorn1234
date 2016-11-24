# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 12:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species_of_animal_can_take', models.CharField(default='dog', max_length=10)),
                ('gender', models.CharField(max_length=1)),
                ('number_of_pet_own', models.IntegerField()),
                ('dwelling', models.CharField(max_length=10)),
                ('has_yard', models.BooleanField(default=False)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='/media/usergalary/default_profile.png', upload_to='usergalary')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]