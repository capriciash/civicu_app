# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labelgame', '0005_image_date_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date_taken',
            field=models.DateField(default=None),
        ),
    ]
