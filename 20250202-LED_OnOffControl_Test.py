#!/usr/bin/env python3


#2025/02/02 



from gpiozero import LED
from time import sleep

# グローバル変数としてLEDインスタンスのリストを作成
leds = []

def setup_leds():
    global leds  # グローバル変数を明示的に使用
    pin_numbers = [17, 22, 27]  # 使用するGPIOピン
    leds = [LED(pin) for pin in pin_numbers]

def turn_on_all():
    for led in leds:
        led.on()
        sleep(0.2)

def turn_off_all():
    for led in leds:
        led.off()

# 初期設定
setup_leds()

# テスト
turn_on_all()  # 全てのLEDをON
