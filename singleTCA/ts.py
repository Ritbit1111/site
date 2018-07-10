# -*- coding: utf-8 -*-
from singleTCA.models import CF, T_PS, V_REV_SP
from singleTCA.serializers import CFSerializer, T_PSSerializer, V_REV_SPSerializer
import pandas as pd

def TranSerialization(path, portfolio):
    CF.objects.all().delete()
    T_PS.objects.all().delete()
    V_REV_SP.objects.all().delete()
    df = pd.read_csv(path)
    #df = df.fillna('')
    if portfolio[:2] == "CF":
#        CF.objects.create(DateTime=str(list(df["DateTime"])), RIC=str(list(df["RIC"])), FutMktPrice=str(list(df["FutMktPrice"])), FutMktVolume=str(list(df["FutMktVolume"])), CashMktPrice= str(list(df["CashMktPrice"])), CashMktVolume= str(list(df["CashMktVolume"])), FutExecQty=str(list(df["FutExecQty"])), FutExecFillPrice=str(list(df["FutExecFillPrice"])), FutExecSide=str(list(df["FutExecSide"])), CashExecQty=str(list(df["CashExecQty"])), CashExecFillPrice=str(list(df["CashExecFillPrice"])), CashExecSide=str(list(df["CashExecSide"])))
        CF.objects.create(Columns=list(df.columns),Data=df.values.tolist())
        frame = CF.objects.all()
        serializer = CFSerializer(frame, many=True)
    
    elif portfolio[:2] == "%T" or  portfolio[:2] == "PS":
#        T_PS.objects.create(DateTime=str(list(df["DateTime"])),RIC=str(list(df["RIC"])), MktPrice= str(list(df["MktPrice"])), MktVolume= str(list(df["MktVolume"])),  ExecQty=str(list(df["ExecQty"])), ExecFillPrice=str(list(df["ExecFillPrice"])),ExecSide=str(list(df["ExecSide"])), mkt_cum_volume= str(list(df["mkt_cum_volume"])), sliced_mkt_cum_volume= str(list(df["sliced(order)_mkt_cum_volume"])), mkt_price_sumprod= str(list(df["mkt_price_sumprod"])), mkt_vwap= str(list(df["mkt_vwap"])), exec_cum_volume= str(list(df["exec_cum_volume"])), exec_price_sumprod = str(list(df["exec_price_sumprod"])), exec_vwap = str(list(df["exec_vwap"])))
        T_PS.objects.create(Columns=list(df.columns),Data=df.values.tolist())
        frame = T_PS.objects.all()
        serializer = T_PSSerializer(frame, many=True)
    
    elif portfolio[:2] == "%V" or  portfolio[:3] == "REV" or portfolio[:2] == "SP" :
#        V_REV_SP.objects.create(DateTime=str(list(df["DateTime"])), RIC=str(list(df["RIC"])), FutMktPrice=str(list(df["FutMktPrice"])), FutMktVolume=str(list(df["FutMktVolume"])), FutExecQty=str(list(df["FutExecQty"])), FutExecFillPrice=str(list(df["FutExecFillPrice"])), FutExecSide=str(list(df["FutExecSide"])),  mkt_cum_volume=str(list(df["mkt_cum_volume"])), sliced_mkt_cum_volume=str(list(df["sliced(order)_mkt_cum_volume"])), mkt_price_sumprod=str(list(df["mkt_price_sumprod"])), mkt_vwap=str(list(df["mkt_vwap"])), exec_cum_volume=str(list(df["exec_cum_volume"])), exec_price_sumprod = str(list(df["exec_price_sumprod"])), exec_vwap = str(list(df["exec_vwap"])))
        
        V_REV_SP.objects.create(Columns=list(df.columns),Data=df.values.tolist())
        frame = V_REV_SP.objects.all()
        serializer = V_REV_SPSerializer(frame, many=True)
    return serializer