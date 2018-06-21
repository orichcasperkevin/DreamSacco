# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-08 06:02
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0014_accountsprofile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+2547########', max_length=128),
        ),
    ]
