# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-10 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0026_auto_20180310_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsprofile',
            name='accountNumber',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
