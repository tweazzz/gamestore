# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-13 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20180206_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='store.Category'),
            preserve_default=False,
        ),
    ]
