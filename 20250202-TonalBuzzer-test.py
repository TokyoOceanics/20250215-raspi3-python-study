#!/usr/bin/env python

#https://www.denshi.club/parts/2020/11/gpiozero6import-tonalbuzzer.html

from gpiozero import TonalBuzzer
from time import sleep

low_freq=220
high_freq=880
freq_step=2
duration=0.00001


bz=TonalBuzzer(23, initial_value=1.0)

while True:

    try:
        for i in range(low_freq,high_freq,freq_step):
            try:
                bz.play(i)
                sleep(duration)
            except Exception as e:
                print(f"tone value=",i,"  Error is ",{e})
                exit()

        for i in range(high_freq,low_freq,-freq_step):
            try:
                bz.play(i)
                sleep(duration)
            except Exception as e:
                print(f"tone value=",i,"  Error is ",{e})
                exit()

    except KeyboardInterrupt:
        bz.stop()
        print("Keyboard Interrupt detected.")
        exit()

"""
bz.play(220)
sleep(1.0)
bz.play(440)
sleep(1.0)
bz.play(880)
sleep(1.0)
bz.stop()
"""