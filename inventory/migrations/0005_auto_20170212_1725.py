# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_restaurant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='offer',
            field=models.TextField(default='N/A'),
        ),
    ]
