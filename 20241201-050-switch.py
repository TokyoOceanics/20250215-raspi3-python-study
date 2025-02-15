#!/usr/bin/env python3

from gpiozero import Button

button = Button(21) #SW2
#button.pull_up=True

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")