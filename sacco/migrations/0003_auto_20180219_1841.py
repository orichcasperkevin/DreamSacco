# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-19 18:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0002_auto_20180217_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdeposit',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AccountDeposits', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accountsprofile',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountsProfiles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='loandeposit',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoanDeposits', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='loansprofile',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoansProfiles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
