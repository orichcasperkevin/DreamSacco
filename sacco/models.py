# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class loanRates(models.Model):
   percentageRate=models.FloatField(default=1.00)
class M_pesaConfirmationPINs(models.Model):
    pin=models.CharField(max_length=8,unique=True)
    amountAsociated = models.IntegerField(default=0)
class Accounts(models.Model):
    accountName = models.CharField(max_length=50,unique=True)

class Loans(models.Model):
    loanName = models.CharField(max_length=50,unique=True)

class paymentMethod(models.Model):
    method = models.CharField(max_length=50,unique=True)

class AccountsProfile(models.Model):
    username=models.ForeignKey(User,related_name="accountsProfiles")
    accountName=models.ForeignKey(Accounts,related_name="accountsProfiles")
    phone_number = PhoneNumberField(default='+2547########')
    accountNumber=models.IntegerField(default=0,unique=True)
    creationTime= models.DateTimeField(auto_now_add=True)
    amount=models.FloatField(default=0.0)

class LoansProfile(models.Model):
    username=models.ForeignKey(User,related_name="LoansProfiles")
    loanName=models.ForeignKey(Loans,related_name="LoansProfiles")
    loanNumber = models.IntegerField( default = 0)
    amount=models.FloatField(default=0.0)
    paymentPlan=models.FloatField(default=0.0)
    paymentTime =   models.IntegerField( default = 0)
    remainingAmount = models.FloatField(default=0)
    creationTime = models.DateTimeField(auto_now_add=True)


class LoanDeposit(models.Model):
    username = models.ForeignKey(User,related_name="LoanDeposits")
    loanName = models.ForeignKey(Loans,related_name="LoanDeposits")
    loanNumber = models.ForeignKey(LoansProfile,related_name="LoanDeposits",default=0)
    ammount = models.FloatField(default=0.0)
    depositTime = models.DateTimeField(auto_now_add=True)
    paymentMethod = models.ForeignKey(paymentMethod,related_name="LoanDeposits")

class AccountDeposit(models.Model):
    username = models.ForeignKey(User,related_name="AccountDeposits")
    accountName = models.ForeignKey(Accounts,related_name="AccountDeposits")
    accountNumber = models.ForeignKey(AccountsProfile,related_name="AccountDeposits")
    ammount = models.FloatField(default=0.0)
    depositTime = models.DateTimeField(auto_now_add=True)
    paymentMethod = models.ForeignKey(paymentMethod,related_name="AccountDeposits")
