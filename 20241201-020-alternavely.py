#!/usr/bin/env python3
from gpiozero import LED
from signal import pause
red=LED(17)
red.blink(0.1 )
pause()