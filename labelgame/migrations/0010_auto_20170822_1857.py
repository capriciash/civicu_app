# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labelgame', '0009_auto_20170822_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chosen_label', models.CharField(choices=[('Wolf', 'Wolf'), ('Bear', 'Bear'), ('Monkey', 'Monkey'), ('Not an Animal', 'NotAnimal'), ('Skipped', 'Skipped')], default='Skipped', max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='userlabel',
            name='sel_animal',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='labelgame.Animals'),
        ),
    ]
