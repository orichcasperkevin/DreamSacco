# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-07 20:09
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0007_auto_20180307_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+25473#######', max_length=128),
        ),
    ]
