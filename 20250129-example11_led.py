#!/usr/bin/env python3

port=27

from gpiozero import LED
from time import sleep
from sys import argv

print(argv[0])
if len(argv)>=2 :
    port=int(argv[1])
led=LED(port)

try:
    while True:
        b=led.value
        b=int(not(b))
        print('GPIO'+str(port),'=',b)
        led.value=b
        sleep(0.5)

except KeyboardInterrupt:
    print('KeyboardInterrupt')
    led.close()
    exit()