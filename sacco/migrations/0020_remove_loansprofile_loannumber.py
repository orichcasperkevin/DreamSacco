# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-09 08:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0019_loansprofile_loannumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loansprofile',
            name='loanNumber',
        ),
    ]