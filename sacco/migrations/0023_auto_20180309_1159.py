# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-09 11:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0022_remove_loansprofile_loannumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='loandeposit',
            name='loanNumber',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='LoanDeposits', to='sacco.LoansProfile'),
        ),
        migrations.AddField(
            model_name='loansprofile',
            name='loanNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='loansprofile',
            name='paymentTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
