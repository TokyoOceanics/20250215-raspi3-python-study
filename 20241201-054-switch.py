#!/usr/bin/env python3
from time import sleep
from gpiozero import Button

# ボタンの初期化
button = Button(21, pull_up=True)  # SW2
button_white = Button(24, pull_up=False)  # SW1

# ボタンが押されたときの動作
def on_button_pressed():
    print("Button SW2 pressed!")

def on_button_white_pressed():
    print("Button SW1 pressed!")

# ボタンにコールバックを設定
button.when_pressed = on_button_pressed
button_white.when_pressed = on_button_white_pressed

# ボタンの状態をモニタリング
try:
    while True:
        print(f"Button value: {button.value}, Button White value: {button_white.value}")
        sleep(0.1)
except KeyboardInterrupt:
    print("\nExiting program.")

