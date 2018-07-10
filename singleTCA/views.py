from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView
from singleTCA.ts import TranSerialization

import pandas as pd
import os
import json
from django.http import Http404
import csv
import ast

from singleTCA.forms import *

def date_acc_view(request):
# Function to just display the first page
    if request.method == 'GET':
        accform = acc_date_Form()
        return render(request, 'user_form.html', {"accform": accform})
    else:
        return HttpResponseRedirect('/login')

def portfolio_view(request):
    if request.method == 'POST':

        form = acc_date_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            acc_no = data['account_id']
            if(os.path.isdir(str(data['date']).replace('-',''))):
                port_path = str(data['date']).replace('-','') + "/PortAccMap.csv"
                df_portmap = pd.read_csv(port_path)
                portfolio_list = list(df_portmap.loc[df_portmap['AccountID'].str.contains(str(acc_no))]['FIX_440'])
                if len(portfolio_list) ==0:
                    return(HttpResponse("No trading data for account ID: {} on date: {} ".format(acc_no, str(data['date']))))  
                else:
                    CHOICES = [(a,a) for a in portfolio_list]
                    empty_label = "---Select---"
                    CHOICES = list([(u'', empty_label)] + CHOICES)
                    port_form = portfolio_Form(initial={'date':data['date'], 'account_id':data['account_id']}, choice_tuple=CHOICES) 
                    return (render(request, 'portfolio_list.html', {"port_form": port_form}))
                    
                                
            else:
                link="/singledayTCA"
                return(HttpResponse("No data for this date available<br>Click on this link to get back the TCA Form <a href={}>TCA_REPORT</a>".format(link)))
            
        else:
            return(HttpResponse("Form not valid"))
    else:
        return (HttpResponseRedirect('/login'))
        
def instrument_view(request):
    if request.method == 'POST':
        CHOICES = (
                  )
        form = portfolio_Form(request.POST or None, choice_tuple=CHOICES)
        if form.is_valid():
            data = form.cleaned_data
            portfolio = data['portfolio']
            port_path = str(data['date']).replace('-','') + "/PortAccMap.csv"
            df_portmap = pd.read_csv(port_path)
            
            portfolio_list = df_portmap.loc[df_portmap['AccountID'].str.contains(str(data['account_id']))]
            instruments_string = list (portfolio_list.loc[df_portmap['FIX_440'].str.contains(str(portfolio))]['Ins'])[0]
            instruments_list= instruments_string.split(', ')
            CHOICES =  [(a,a) for a in instruments_list]
            empty_label = "---Select---"
            CHOICES = list([(u'', empty_label)] + CHOICES)
            ins_form = instrument_Form(initial={'date':data['date'], 'account_id':data['account_id'], 'portfolio':data['portfolio']}, choice_tuple=CHOICES)

            return (render(request, 'instruments_list.html', {"ins_form": ins_form}))

        else:
            link="/home"
            return(HttpResponse("Form not valid<br>Click on this link to get back the TCA Form <a href={}>TCA_FORM</a>".format(link)))
    else:
        return (HttpResponseRedirect('/login'))
        
def summary_view(request):
    if request.method == 'POST':
        
        CHOICES = (
                  )
        
        form = instrument_Form(request.POST or None, choice_tuple=CHOICES)
        if form.is_valid():
            data = form.cleaned_data
            path_summary   = str(data['date']).replace('-','') + '/Portfolio/' + data['portfolio'] + '/' + data['instrument'] + '/data.csv'
            path_data      =  str(data['date']).replace('-','') + '/Portfolio/' + data['portfolio'] + '/' + data['instrument'] + '/DataSummary.csv'
            if os.path.isfile(path_summary)==True:
                df_summary = pd.read_csv(path_summary)
                df_summary = df_summary.applymap(str)
                summary_array = [list(df_summary.columns), list(df_summary.ix[0])]
                
                t_serializer = TranSerialization(path_data, data['portfolio'])
                serial_json  = t_serializer.data
                cols = serial_json[0]['Columns']
                rows = serial_json[0]['Data'].replace('nan','None')
                rows = ast.literal_eval(rows[1:-1])
                data_array = [ast.literal_eval(cols)]
                for item in range(len(rows)):
                    data_array.append(rows[item])
                locked_form = show_Form(initial={'date':data['date'], 'account_id':data['account_id'], 'portfolio':data['portfolio'], 'instrument':data['instrument']})

                return (render(request, 'summary.html',  {'dfjson_summary': json.dumps(summary_array), 'dfjson_data': json.dumps(data_array), 'csv':path_summary, 'portfolio':data['portfolio'], 'ins':data['instrument'], 'dt':str(data['date']), 'locked_form':locked_form}))
            else:
                link="/home"
                return(HttpResponse("No file summary <br>Click on this link to get back the TCA Form <a href={}>TCA_FORM</a>".format(link)))

        else:
            link="/home"
            return HttpResponse("Form not valid<br>Click on this link to get back the TCA Form <a href={}>TCA_FORM</a>".format(link))
    else:
        return (HttpResponseRedirect('/login'))
     
def download(request):
    if request.method == 'POST':
        path = request.POST.get("csv")
        port = request.POST.get("portfolio")
        ins  = request.POST.get("ins")
        dt   = request.POST.get("dt")
        print (path)
        if os.path.exists(str(path)):
            with open(path, 'rb') as myfile:
                response = HttpResponse(myfile, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="TCA{}/{}/{}.csv"'.format(dt, port, ins)
                return response
            
    raise Http404