#!/usr/bin/env python3
from time import sleep

from gpiozero import Button

button = Button(21) #SW2
button_white=Button(24, pull_up=False) #SW1

#button.pull_up=True
#button_white.pull_up=False

#while button.value==0:
#    pass

while True:
    print('sw2',end=' ')
    print(button.value)
    print('sw1',end=' ')
    print(button_white.value)
    
    
    sleep(0.1)
    
    
    
print("Button pressed")
