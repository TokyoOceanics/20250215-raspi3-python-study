#!/usr/bin/env python3

port=27
b=0

from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)
GPIO.setup(port, GPIO.OUT)

while True:
    b=int(not(b))
    print('GPIO'+str(port),'=',b)
    GPIO.output(port,b)
    sleep(0.5)