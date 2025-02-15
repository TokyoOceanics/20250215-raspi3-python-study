#!/usr/bin/env python3

from gpiozero import Button
from time import sleep

button1=Button(24, pull_up=False)
button2=Button(21, pull_up=True)

while True:
   # print("button1(pull-down  )",button1.value)
   # print("button2(pull-up    )",button2.value)
   print(button1, button2) 
   sleep(1)