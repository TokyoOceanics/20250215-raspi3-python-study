#!/usr/bin/env python3


import requests

url_s='https://bokunimo.net/iot/cq/test.json'

res=requests.get(url_s)
res_dict=res.json()
res.close()

print('title:',res_dict.get('title'))
print('descr:',res_dict.get('descr'))
print('state:',res_dict.get('state'))
print('url:',res_dict.get('url'))
print('date:',res_dict.get('date'))
