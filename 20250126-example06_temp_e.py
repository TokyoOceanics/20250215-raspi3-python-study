#!/usr/bin/env python3

#filename='/sys/class/thermal/thermal_zone0/temp'
filename='/sys/class/thermal/thermal_zone0/temp'

try:
    fp=open(filename)

except Exception as e:
    print(e)
    exit()

temp=float(fp.read())/1000
fp.close()

print('Temperature=',temp)
