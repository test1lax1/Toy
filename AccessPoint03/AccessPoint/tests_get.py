from django.test import TestCase

# Create your tests here.
from django.test import TestCase
import requests 
import time
import datetime
import pandas as pd
import numpy as np
from pandas import DataFrame

from itertools import cycle, islice


#url = ('http://127.0.0.1:8000/AccessPoint03/AccessPoint/')
#r = requests.get(url) 
##print(r.content)
url = ('http://127.0.0.1:8000/AccessPoint03/AreaBandWidthDetails/')
#import json
filepath = r"C:\Users\Surya\Desktop\laxman\AppData.csv"
df = pd.read_csv(filepath)
##print(df.head(20))
##tac = df.groupby('Tac')
##print(df['Tac'].value_counts())
a = df.groupby('Tac').agg({'BandWidth':"sum"},index = True)
tac_city = {'311344534':'Boston','32276891':'NewYork','334455111':'Austin','343536222':'NewZersy'}

a.reset_index()
print(a.columns)
a.reset_index()
# a.replace(to_replace = '311344534',value = 'Boston')
# a.replace(to_replace = '32276891',value = 'NewYork')
# a.replace(to_replace = '334455111',value = 'Austin')
# a.replace(to_replace = '343536222',value = 'NewZersy')


a.rename(columns = {'Tac':'cityName'}, inplace = True)
a.rename(columns = {'BandWidth':'UsedData'}, inplace = True)
print (a)

#data = a.to_json(orient='records')
#print ("printing Json Data")
#print (d)
#data = {"cityName" : "Bosten","UsedData" : 123456890 }
#r = requests.post(url, json = data) 
#print(r.content)


