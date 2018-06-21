from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AccountsProfile
from datetime import datetime
from .models import Accounts,M_pesaConfirmationPINs

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class meta :
        model = User
        fields = ('username','password')



class RegisterForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())


    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')

class makePaymentForm(forms.Form):
    PIN = forms.CharField(required=True)
    def clean_PIN(self):
     cd = self.cleaned_data
     PIN = cd.get('PIN')
     for object in M_pesaConfirmationPINs.objects.all():
         if object.pin == PIN:
             return PIN

     else :
            raise forms.ValidationError("M-Pesa confirmation PIN does not exist ")
class loanApplicationForm(forms.Form):
    my_Loan_choices=(('emergency loan','emergency loan'),
                   ('normal loan','normal loan'),
                    ('advance loan','advance loan'))
    loanName = forms.ChoiceField( choices=my_Loan_choices,widget=forms.widgets.Select())
    amountToLoan = forms.IntegerField(required=True)
    paymentPlanPerMonth = forms.IntegerField(required=True)
    paymentPeriod = forms.IntegerField(required=True)


    def clean_amountToLoan(self):
        cd = self.cleaned_data
        amountToLoan = cd.get('amountToLoan')
        if amountToLoan >10000:
                raise forms.ValidationError("maximum borrowing amount for this loan is 10,000 ")
        if amountToLoan < 500:
                raise forms.ValidationError("minimum borrowing amount is 500")
        return amountToLoan

    def clean_paymentPlanPerMonth(self):
        cd = self.cleaned_data
        amountToLoan = cd.get('amountToLoan')
        paymentPlanPerMonth = cd.get('paymentPlanPerMonth')
        if paymentPlanPerMonth > amountToLoan:
            raise forms.ValidationError("payment plan per month cant be more than amount borrowed")
        return paymentPlanPerMonth

    def clean_paymentPeriod(self):
        cd = self.cleaned_data
        paymentPeriod = cd.get('paymentPeriod')
        if paymentPeriod > 6 :
            raise forms.ValidationError("this loan must be paid within 6 months")
        return paymentPeriod

class AccountCreationForm(forms.Form):
    my_City_choices=(('1','Nairobi'),
               ('2','Mombasa'),
               ('3','Eldoret'),
               ('4','Nakuru'),
               ('5','Kitale'),
               ('6','Kisumu'))
    my_Nation_choices=(('1','KENYAN'),
                            ('2','OTHERS'))
    my_Marital_choices=(('1','married'),
               ('2','single'),
               ('3','engaged'))
    my_Account_choices=(('fixed Deposit Account','fixed Deposit Account'),
               ('helb','helb'),
                ('education savings account','education savings account'),
               ('main savings account','main savings account'))

    phone_number = forms.CharField(required=True)
    accountName = forms.ChoiceField( choices=my_Account_choices,widget=forms.widgets.Select())
    nationalIdNumber= forms.CharField(required=True)
    city = forms.ChoiceField( choices=my_City_choices,widget=forms.widgets.Select())
    nationality = forms.ChoiceField( choices=my_Nation_choices,widget=forms.widgets.Select())
    marital_status = forms.ChoiceField( choices=my_Marital_choices,widget=forms.widgets.Select())
    def clean_nationalIdNumber(self):
        cd = self.cleaned_data
        nationalIdNumber=cd.get('nationalIdNumber')
        if len(nationalIdNumber) != 8:
            raise forms.ValidationError("the ID number you entered is invalid ")

        return nationalIdNumber
