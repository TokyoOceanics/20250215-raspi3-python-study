#!/usr/bin/env python3

ambient_chid='87934'
ambient_wkey='6588f810bd4ae9ed'
ambient_tag='d1'

import urllib.request
import json

filename='/sys/class/thermal/thermal_zone0/temp'
url_s='https://ambidata.io/api/v2/channels/'+ambient_chid+'/data'
head_dict={'Content-Type':'application/json'}
body_dict={'writeKey':ambient_wkey, ambient_tag:0.0}


try:
    fp=open(filename)
except Exception as e:
    print(e)
    exit()
temp=float(fp.read())/1000
fp.close()
print("temperature=", temp)

body_dict[ambient_tag]=temp
print(head_dict)
print(body_dict)
post=urllib.request.Request(url_s, json.dumps(body_dict).encode(), head_dict)

try:
    res=urllib.request.urlopen(post)

except Exception as e:
    print(e, url_s)
    exit()

res_str=res.read().decode()
res.close()

if(len(res_str)):
    print('Response:', res_str)
else:
    print('Done')
    
print(res_str)




           