#!/usr/bin/env python3
from gpiozero import PWMLED
from time import sleep
led=PWMLED(17)
duty=0.0
while True:
    if(duty>0.9):
        duty=0.0
    else:
        duty+=0.05
    led.value=duty;
    print(duty)
    sleep(0.01)