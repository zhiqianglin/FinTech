# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20170212_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='url',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.TextField(default='N/A', max_length=200),
        ),
    ]
