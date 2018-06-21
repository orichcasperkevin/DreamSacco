# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,Http404
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm,RegisterForm,AccountCreationForm,loanApplicationForm,makePaymentForm
# Create your views here.
from .models import *
from django.core.mail import send_mail
import random
# Create your views here.
@login_required
def user_profile(request,username):
    object = User.objects.get(username=username)
    return render(request,'user_page.html',{'object':object})
@login_required
def accountDeposit(request,username):
    object = AccountsProfile.object.get(username=username)
    return render(request,'accountDeposit.html',{'object':object})
@login_required
def contact(request):
    return render(request,'contact.html')

def loanApplication(request,username):
    object = User.objects.get(username=username)
    if request.method == 'POST':
        form = loanApplicationForm(request.POST)
        if form.is_valid():
            percentageRate = loanRates.objects.get(id=1)
            print percentageRate
            ratedLoan = form.cleaned_data['amountToLoan'] + (form.cleaned_data['amountToLoan'] * (percentageRate.percentageRate/100))
            loanNameChoice = form.cleaned_data['loanName']
            newLoan = LoansProfile(username=object,
                                     loanName=Loans.objects.get(loanName=loanNameChoice),
                                      amount= form.cleaned_data['amountToLoan'],
                                       paymentPlan=form.cleaned_data['paymentPlanPerMonth'],
                                       paymentTime=form.cleaned_data['paymentPeriod'],
                                       loanNumber = random.randint(299,39999),
                                       remainingAmount = ratedLoan)
            newLoan.save()
            return redirect('user_profile',username=object)
    else:
            form = loanApplicationForm
    return render(request,'loanRegister.html',{'object':object,'form':form})

def loanPayment(request,username,loanNumber):
    object1=User.objects.get(username=username)
    object2 = LoansProfile.objects.get(username=object1,loanNumber=loanNumber)
    totalAmountPayedForThisLoan = 0
    if request.method == 'POST':
        form = makePaymentForm(request.POST)

        if form.is_valid():
            currentLoanAmount = object2.remainingAmount

            cd = form.cleaned_data
            validtransaction =  M_pesaConfirmationPINs.objects.get( pin = cd['PIN'])
            newLoanDeposit = LoanDeposit(username=object1,
                                          loanName= Loans.objects.get(loanName = object2.loanName.loanName),
                                          loanNumber = object2,
                                           ammount = validtransaction.amountAsociated,
                                            paymentMethod= paymentMethod.objects.get(method="m_pesa"))

            object2.remainingAmount = (currentLoanAmount - newLoanDeposit.ammount)
            remainingAmount =  object2.remainingAmount

            if (remainingAmount < 0) :
                object2.remainingAmount = 0
                object3 = AccountsProfile.objects.get(username=object1,id=1)
                amount = object3.amount
                object3.amount = (amount + (0 - remainingAmount))
                newAccountDeposit = AccountDeposit(username=object1,
                                              accountName= Accounts.objects.get(accountName = object3.accountName.accountName),
                                               ammount = (0-remainingAmount),
                                               accountNumber=AccountsProfile.objects.get(accountNumber=object3.accountNumber),
                                                paymentMethod = paymentMethod.objects.get(method="m_pesa"))
                newAccountDeposit.save()
                message =  'dear customer DREAM SACCO wishes to inform you that you overpaid your loan.This amount has been transfered to your one of your accounts. log on to your DREAM SACCO online to view this changes.'
                send_mail(
                  'loan over Pay',
                   message,
                  'orichcasper@gmail.com',
                   [object1.email,],
                   fail_silently=False,)
                object3.save()
            object2.save()
            newLoanDeposit.save()
            return redirect('user_profile',username=object1)
    else:
        form=makePaymentForm(request.POST)
    return render(request,'loanPayments.html',{'object2':object2,'form': form})
def accountDeposit(request,username,accountNumber):
        object1=User.objects.get(username=username)
        object2 = AccountsProfile.objects.get(username=object1,accountNumber=accountNumber)
        if request.method == 'POST':
            form = makePaymentForm(request.POST)

            if form.is_valid():
                currentAccountAmount = object2.amount
                cd = form.cleaned_data
                validtransaction =  M_pesaConfirmationPINs.objects.get( pin = cd['PIN'])
                newAccountDeposit = AccountDeposit(username=object1,
                                              accountName= Accounts.objects.get(accountName = object2.accountName.accountName),
                                               ammount = validtransaction.amountAsociated,
                                               accountNumber=AccountsProfile.objects.get(accountNumber=object2.accountNumber),
                                                paymentMethod = paymentMethod.objects.get(method="m_pesa"))

                object2.amount = (currentAccountAmount + newAccountDeposit.ammount)
                object2.save()
                newAccountDeposit.save()
                return redirect('user_profile',username=object1)
        else:
            form=makePaymentForm(request.POST)
        return render(request,'accountPayment.html',{'object2':object2,'form': form})

def accountCreation(request,username):
    object = User.objects.get(username=username)
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():

            accountNameChoice = form.cleaned_data['accountName']
            newAccount = AccountsProfile( username = object,
                                          accountName = Accounts.objects.get(accountName=accountNameChoice),
                                           phone_number = form.cleaned_data['phone_number'],
                                           accountNumber = random.randint(299,39999),
                                           amount=0 )
            newAccount.save()
            return redirect('user_profile',username=object)
    else:
        form = AccountCreationForm()

    return render(request,'accountDeposit.html',{'object':object,'form': form})

def index(request):
 if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
       cd = form.cleaned_data
       user = authenticate(username=cd['username'],password=cd['password'])
       if user is not None:
          if user.is_active:
             login(request, user)
             return redirect('user_profile',username=user.username )
          else:
             return HttpResponse('Disabled account')
       else:
             return HttpResponse('Invalid login')
 else:
  form = LoginForm()
 return render(request, 'index.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})
