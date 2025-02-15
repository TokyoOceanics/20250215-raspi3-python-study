#!/usr/bin/env python3


import urllib.request
import json

url_s='https://bokunimo.net/iot/cq/test.json'

res=urllib.request.urlopen(url_s)
res_dict=json.loads(res.read().decode())
res.close()

print('title:',res_dict.get('title'))
print('descr:',res_dict.get('descr'))
print('state:',res_dict.get('state'))
print('url:',res_dict.get('url'))
print('date:',res_dict.get('date'))
