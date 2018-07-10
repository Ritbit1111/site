# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from singleTCA.models import Info, CF, T_PS, V_REV_SP
from rest_framework import serializers


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('date', 'acc_no', 'portfolio', 'ins')
        
class CFSerializer(serializers.ModelSerializer):
    class Meta:
        model = CF
        fields = ('Columns',	'Data')
        
class T_PSSerializer(serializers.ModelSerializer):
    class Meta:
        model = T_PS
        fields = ('Columns',	'Data')
        
class V_REV_SPSerializer(serializers.ModelSerializer):
    class Meta:
        model = V_REV_SP
        fields = ('Columns',	'Data')