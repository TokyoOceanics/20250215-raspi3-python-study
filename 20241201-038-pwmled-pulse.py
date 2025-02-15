#!/usr/bin/env python3

from gpiozero import PWMLED
from signal import pause

led=PWMLED(17)

led.pulse()

pause()