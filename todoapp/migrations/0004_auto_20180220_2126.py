# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_auto_20180220_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtodolist',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
