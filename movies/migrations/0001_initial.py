# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('title', models.TextField()),
                ('subject', models.CharField(default='', max_length=255)),
                ('actor', models.CharField(default='', max_length=255)),
                ('actress', models.CharField(default='', max_length=255)),
                ('director', models.CharField(default='', max_length=255)),
                ('popularity', models.IntegerField()),
                ('awards', models.BooleanField()),
                ('image', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
