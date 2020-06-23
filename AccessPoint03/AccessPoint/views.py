# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from AccessPoint.models import AreaBandWidthDetails,AccessPoint
from AccessPoint.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response



class AccessPointView(viewsets.ModelViewSet):
    queryset = AccessPoint.objects.all()
    print(queryset)
    serializer_class = AccessPointSerializer    
    print ("access piont View")
    
class AreaBandwidthView(viewsets.ModelViewSet):
    queryset = AreaBandWidthDetails.objects.all()
    print(queryset)
    serializer_class = AreaBandWidthSerializer
    

   
    
   