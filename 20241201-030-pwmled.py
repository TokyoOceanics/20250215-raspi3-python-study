#!/usr/bin/env python3
from gpiozero import PWMLED
from time import sleep
led=PWMLED(17)

while True:
    led.value=0 #off
    sleep(1)
    led.value=0.5
    sleep(1)
    led.value=1
    sleep(1)