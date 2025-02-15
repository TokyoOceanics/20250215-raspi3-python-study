#!/usr/bin/env python3


#buzzer
#https://www.denshi.club/parts/2020/11/gpiozero5import-buzzer.html

from gpiozero import Buzzer
from time import sleep

bz=Buzzer(23)
bz.beep()
sleep(3)
print(bz.is_active)