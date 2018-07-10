# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 18:02:55 2018

@author: RiteshPK
"""

from django import forms
import datetime

class acc_date_Form(forms.Form):
    date        = forms.DateField(label = 'Date', initial = datetime.datetime.today(), widget=forms.DateInput(attrs={'type': 'date', 'class':"form-control"}))
    account_id  = forms.CharField(label = 'Account_ID', max_length=15, widget = forms.TextInput(attrs={'required': True, 'class':"form-control", 'placeholder' : "Enter ID"}))
 
class portfolio_Form(forms.Form): 
    def __init__(self, *args, **kwargs):
        choice_tuple = kwargs.pop('choice_tuple')
        
        super(portfolio_Form, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['readonly'] = True
        self.fields['account_id'].widget.attrs['readonly'] = True
        self.fields['portfolio'] = forms.CharField(label = 'Portfolio', widget = forms.Select(choices=choice_tuple, attrs={'class':"form-control", 'id':'sel', 'onchange':"sub()"}))

        
    date        = forms.DateField(label = 'Date', initial = datetime.datetime.today(), widget=forms.DateInput(attrs={'type': 'date', 'class':"form-control"}))
    account_id  = forms.CharField(label = 'Account_ID', max_length=15, widget = forms.TextInput(attrs={'required': True, 'class':"form-control", 'placeholder' : "Enter ID"}))

class instrument_Form(forms.Form):  
    def __init__(self, *args, **kwargs):
        choice_tuple = kwargs.pop('choice_tuple')
        
        super(instrument_Form, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['readonly'] = True
        self.fields['account_id'].widget.attrs['readonly'] = True
        self.fields['portfolio'].widget.attrs['readonly'] = True
        self.fields['instrument'] = forms.CharField(label = 'Script', widget = forms.Select(choices=choice_tuple, attrs={'class':"form-control",  'onchange':"sub()", 'id':'sel'}))

    date        = forms.DateField(label = 'Date', initial = datetime.datetime.today(), widget=forms.DateInput(attrs={'type': 'date', 'class':"form-control"}))
    account_id  = forms.CharField(label = 'Account_ID', max_length=15, widget = forms.TextInput(attrs={'required': True, 'class':"form-control", 'placeholder' : "Enter ID"}))
    portfolio   = forms.CharField(label = 'Portfolio', max_length=15, widget = forms.TextInput(attrs={'required': True, 'class':"form-control", 'placeholder' : "Enter Portfolio"}))
    
class show_Form(forms.Form):
    def __init__(self, *args, **kwargs):        
        super(show_Form, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['readonly'] = True
        self.fields['account_id'].widget.attrs['readonly'] = True
        self.fields['portfolio'].widget.attrs['readonly'] = True
        self.fields['instrument'].widget.attrs['readonly'] = True
        
    date        = forms.DateField(label = 'Date', initial = datetime.datetime.today(), widget=forms.DateInput(attrs={'type': 'date', 'class':"form-control"}))
    account_id  = forms.CharField(label = 'Account_ID', max_length=15, widget = forms.TextInput(attrs={'required': True, 'class':"form-control", 'placeholder' : "Enter ID"}))
    portfolio   = forms.CharField(label = 'Portfolio', max_length=15, widget = forms.TextInput(attrs={'required': True, 'class':"form-control", 'placeholder' : "Enter Portfolio"}))
    instrument  = forms.CharField(label = 'Script', max_length=15, widget = forms.TextInput(attrs={'required': True, 'class':"form-control", 'placeholder' : "Enter Portfolio"}))
    
