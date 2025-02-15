#!/usr/bin/env python3

port=27
b=0

from gpiozero import LED
from time import sleep

led=LED(port)

while True:
    b=int(not(b))
    print('GPIO'+str(port),'=',b)
    led.value=b
    sleep(0.5)