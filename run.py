
#! /usr/bin/env python3
import os
import requests

arr = os.listdir('/data/feedback')
dict = {}
key_values = ("title","name","date","feedback")
for file in arr:
 f = open('/data/feedback/'+file, "r")
 cont = 0
 for line in f:
  if cont == 0:
   dict['title'] = line
  elif cont ==1:
   dict['name'] = line
  elif cont == 2:
   dict['date'] = line
  else:
   dict['feedback'] = line
  cont=cont+1
 response = requests.post(r'http://<url>/feedback/', json=dict)
 print('Response',response.status_code)
 f.close()
