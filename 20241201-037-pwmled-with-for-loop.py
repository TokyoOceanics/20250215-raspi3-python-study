#!/usr/bin/env python3
from gpiozero import PWMLED
from time import sleep
import numpy as np 

led=PWMLED(17)
while True:
    for duty_ratio in np.arange(0.0, 1.0, 0.01):
        led.value=duty_ratio
        sleep(0.01)
    for duty_ratio in np.arange(1.0,0.0, -0.01):
        led.value=duty_ratio
        sleep(0.01)

