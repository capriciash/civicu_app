# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 01:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('labelgame', '0004_auto_20170805_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date_taken',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]