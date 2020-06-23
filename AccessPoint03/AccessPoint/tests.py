from django.test import TestCase

# Create your tests here.
from django.test import TestCase
import requests 
import time
import datetime

url = ('http://127.0.0.1:8000/AccessPoint03/AccessPoint/')


time1 = datetime.time(10, 33, 45)
time2 = datetime.time(11,33,45)
time3 = datetime.time(12,33,45)
time4 = datetime.time(13,33,45)
date1 = datetime.date(2020, 6, 15)
date2 = datetime.date(2020, 6, 15)
date3 = datetime.date(2020, 6, 15)
date4 = datetime.date(2020, 6, 15)

date1 = date1.strftime('%Y-%m-%d')
date2 = date2.strftime('%Y-%m-%d')
date3 = date3.strftime('%Y-%m-%d')
date4 = date4.strftime('%Y-%m-%d')
time1 = time1.strftime("%H:%M:%S")
time2 = time2.strftime("%H:%M:%S")
time3 = time3.strftime("%H:%M:%S")
time4 = time4.strftime("%H:%M:%S")
#print (time)
#print (date)
import random


for i in range(0,10000):
    time = random.choice([time1,time2,time3,time4])
    date = random.choice([date1,date2,date3,date4])
    print (time)
    print (date)
    tac = random.choice(['311344534','32276891','334455111','343536222'])
    from random import randint
    sub_id = str( randint(800000,900000))
    band_width = randint(120000,1500000)
    data = {
        'Tac': tac,
        'Time': time,
        'Date':date,    
        'BandWidth':band_width ,
        'subscriber_id':sub_id,
        }
    print (data)
    r = requests.post(url, json = data) 
    print(r.content)

r = requests.get(url) 
#print(r.content)

import json

import csv

data_parsed = json.loads(r.content)
#print (type(data_parsed[0]))


# open a file for writing

with open(r'C:\Users\Surya\Desktop\laxman\AppData.csv', 'w',newline ='') as App_data:
    
    ## create the csv writer object
    
    csvwriter = csv.writer(App_data)
    
    count = 0
    
    for data in data_parsed:
        if count == 0:
            header = data_parsed[count].keys()
            csvwriter.writerow(header)
            count += 1
            print(data_parsed[count].keys())
        else:
            
            csvwriter.writerow(data_parsed[count].values())
            print(data_parsed[count].values())
            count = count + 1

#App_data.close()



