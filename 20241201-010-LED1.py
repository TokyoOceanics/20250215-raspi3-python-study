#!/usr/bin/env python3
from gpiozero import LED
from time import sleep

red=LED(17)
lcd_backlight=LED(26)

while True:
    red.on()
    lcd_backlight.off()
    sleep(1)
    red.off()
    lcd_backlight.on()
    sleep(0.1)