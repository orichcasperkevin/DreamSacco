# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-09 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0020_remove_loansprofile_loannumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='loansprofile',
            name='loanNumber',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
