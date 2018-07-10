from django.db import models

# Create your models here.
class Info(models.Model):
    date = models.CharField(max_length=12)
    acc_no = models.CharField(max_length=10)
    portfolio = models.CharField(max_length = 10, blank = True, default = "All")
    ins = models.CharField(max_length = 6, blank = True, default = "All")

#File starting with     
class CF(models.Model):
    Columns = models.TextField( null = True, blank = True)
    Data = models.TextField( null = True, blank = True)
#    DateTime = models.TextField(null = True, blank = True)
#    RIC = models.TextField(null = True, blank = True)
#    FutMktPrice = models.TextField(null = True, blank = True)
#    FutMktVolume = models.TextField( null = True, blank = True)
#    CashMktPrice = models.TextField( null = True, blank = True)
#    CashMktVolume = models.TextField( null = True, blank = True)
#    FutExecQty = models.TextField( blank = True, null = True)
#    FutExecFillPrice = models.TextField( blank = True , null = True)
#    FutExecSide = models.TextField(blank = True, null = True)
#    CashExecQty = models.TextField( blank = True, null = True)
#    CashExecFillPrice = models.TextField( blank = True, null = True)
#    CashExecSide =  models.TextField( blank = True, null = True)
    
class T_PS(models.Model):
    Columns = models.TextField( null = True, blank = True)
    Data = models.TextField( null = True, blank = True)
#    MktPrice = models.TextField( null = True, blank = True)
#    MktVolume = models.TextField( null = True, blank = True)
#    ExecQty = models.TextField( blank = True, null = True)
#    ExecFillPrice = models.TextField( blank = True, null = True)
#    ExecSide = models.TextField(blank = True, null = True)
#    mkt_cum_volume = models.TextField( blank = True, null = True)
#    sliced_mkt_cum_volume = models.TextField( blank = True, null = True)
#    mkt_price_sumprod = models.TextField( blank = True, null = True)
#    mkt_vwap = models.TextField( blank = True, null = True)
#    exec_cum_volume = models.TextField(blank = True, null = True)
#    exec_price_sumprod = models.TextField( blank = True, null = True)
#    exec_vwap = models.TextField( blank = True, null = True)
    
class V_REV_SP(models.Model):  
    Columns = models.TextField( null = True, blank = True)
    Data = models.TextField( null = True, blank = True)
#    DateTime = models.TextField( null = True, blank = True)
#    RIC = models.TextField( null = True, blank = True)
#    FutMktPrice = models.TextField( null = True, blank = True)
#    FutMktVolume = models.TextField( null = True, blank = True)
#    FutExecQty = models.TextField( blank = True, null = True)
#    FutExecFillPrice = models.TextField( blank = True , null = True)
#    FutExecSide = models.TextField( blank = True, null = True)
#    mkt_cum_volume = models.TextField( blank = True, null = True)
#    sliced_mkt_cum_volume = models.TextField(blank = True, null = True)
#    mkt_price_sumprod = models.TextField( blank = True, null = True)
#    mkt_vwap = models.TextField( blank = True, null = True)
#    exec_cum_volume = models.TextField( blank = True, null = True)
#    exec_price_sumprod = models.TextField( blank = True, null = True)
#    exec_vwap = models.TextField( blank = True, null = True)
    

    