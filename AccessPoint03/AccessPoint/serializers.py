"""
Book: Django RESTful Web Services
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from rest_framework import serializers
from AccessPoint.models import *


class AccessPointSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model = AccessPoint
        fields = ['Tac', 'Date','Time', 'BandWidth','subscriber_id']
                
    def create(self, validated_data):
        print ("Validated Data for AccessPoint")
        print(validated_data)
        return AccessPoint.objects.create(**validated_data)

    def update(self, instance, validated_data):        
        instance.description = validated_data.get('tac', instance.description)
        instance.release_date = validated_data.get('Date', instance.release_date)
        instance.toy_category = validated_data.get('Time', instance.toy_category)
        instance.was_included_in_home = validated_data.get('BandWidth', instance.was_included_in_home)
        instance.save()
        return instance  
    
class AreaBandWidthSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model = AreaBandWidthDetails
        fields = ['cityName','UsedData']
                
    def create(self, validated_data):
        print ("Validated Data for User Bandwidth")
        print(validated_data)
        return AreaBandWidthDetails.objects.create(**validated_data)

       
        
   
    
