#!/usr/bin/env python3

#2024/12/08 LEDの.sourceがわからない。
#加えて、buttonの値
from gpiozero import LED
from gpiozero import Button
from signal import pause

red_led=LED(17)
lcd_back_light=LED(26)

button=Button(21, pull_up=True)

red_led.source=button
lcd_back_light.source=button

#エラー
#red_led.source=(button.is_active)
#lcd_back_light.source=button.is_active

print(button)
pause()