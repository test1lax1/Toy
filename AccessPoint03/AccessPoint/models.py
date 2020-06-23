from django.db import models

# Create your models here.
class AccessPoint(models.Model):
    Tac = models.CharField(max_length=20)
    Date = models.DateField(null=True, blank=True, default=None)
    Time = models.TimeField(null=True, blank=True, default=None)
    BandWidth = models.IntegerField()
    subscriber_id = models.IntegerField()
    

    #def __str__(self):
        #return '%s: %d' % (self.Tac, self.subscriber_id)
    
class AreaBandWidthDetails(models.Model):
    cityName = models.CharField(max_length =50)
    UsedData = models.IntegerField()
    
    def __str__(self):
        return '%s: %d' % (self.cityName, self.UsedData)    
    
