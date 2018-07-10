from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
import datetime as dt
import pandas as pd
import os.path
from multipleTCA.forms import *

import logging

logger = logging.getLogger(__name__)

class FormView(View):
    
    template_name = 'multipleTCA/index.html'
    form = acc_date_Form

    def get(self, request, *args, **kwargs):
        logger.debug("{} entered multiple form".format(request.user.username))
        form = self.form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            start_date = data["start_date"]
            end_date = data["end_date"]
            id_list = data["account_id"]
            request.session['sd'] = str(start_date)
            request.session['ed'] = str(end_date)
            request.session['id'] = id_list
            return HttpResponseRedirect('/multipledayTCA/summary')

        return render(request, self.template_name, {'form': form})

class Summary(View):
    template_name = 'multipleTCA/summary.html'
    form = acc_date_Form
    
    def post(self, request, *args, **kwargs):
        '''Won't allow GET request to enter this url'''
        return HttpResponseRedirect('/TCA/login')
    
    def concat(self, start_date, end_date):
        
        delta = end_date - start_date
        datelist = []
        for i in range(delta.days + 1):
            d = start_date + dt.timedelta(i)
            if d.weekday()<5 :
                datelist.append(d)
        
        dates_string=[str(dates).replace("-", "") for dates in datelist]
        path_list = ["data/{}/".format(dates) for dates in dates_string]

        # Filtering path for existing folders
        path_list = [path for path in path_list if (os.path.isdir(path))]
        df = pd.DataFrame()

        for path in path_list:
            df = df.append(pd.read_csv(path+"PortAccMap.csv"))

        return path_list, df
    
    def get(self, request, *args, **kwargs):

        start_date      = request.session.get("sd")
        end_date        = request.session.get("ed")
        id_list         = request.session.get("id")

        start_date = dt.datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = dt.datetime.strptime(end_date, '%Y-%m-%d').date()
        path_list, df   = self.concat(start_date, end_date)
        df = df.reset_index(drop=True)
        df.to_csv('accumulated_portaccmap.csv')
            
        port_ins_dict = dict.fromkeys(id_list)
            
        for id in id_list:
            port_ins_dict[id] = []
            for i in range(len(df.index)):
                if id in [port.strip() for port in str(df['AccountID'].ix[i]).split(',') if port.strip()]:
                    port_ins_dict[id].append((df['FIX_440'].ix[i], [port.strip() for port in str(df['Ins'].ix[i]).split(',') if port.strip()] ))
            #####Begin from port_ins_dict#########

        for id in id_list:
            print ("------------------******************------------------************")
            print (port_ins_dict[id])
        return render(request, self.template_name, {'id_list': id_list, 'df':df}) 
