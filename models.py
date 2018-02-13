# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Users(models.Model):
    UserID = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class Accounts(models.Model):
    accountName = models.CharField(max_length=50,unique=True)
    accountID = models.CharField(max_length=20,unique=True)

class Loans(models.Model):
    loanName = models.CharField(max_length=50,unique=True)

class LoansProfile(models.Model):
    UserID = models.ForeignKey(Users,related_name="LoansProfiles")
    loanName = models.ForeignKey(Loans)

class AccountsProfile(models.Model):
    UserID = models.ForeignKey(Users,related_name="AccountsProfiles")
    accountName = models.ForeignKey(Accounts)

class paymentMethod(models.Model):
    method = models.CharField(max_length=50,unique=True)

class LoanDeposit(models.Model):
    depositID = models.CharField(max_length=20,unique=True)
    loanName = models.ForeignKey(Loans,related_name="LoanDeposits")
    UserID = models.ForeignKey(Users,related_name="LoanDeposits")
    depositTime = models.DateTimeField(auto_now_add=True)
    paymentMethod = models.ForeignKey(paymentMethod,related_name="LoanDeposits")

class AccountDeposit(models.Model):
    depositID = models.CharField(max_length=20,unique=True)
    loanName = models.ForeignKey(Loans,related_name="AccountDeposits")
    UserID = models.ForeignKey(Users,related_name="AccountDeposits")
    depositTime = models.DateTimeField(auto_now_add=True)
    paymentMethod = models.ForeignKey(paymentMethod,related_name="AccountDeposits")
