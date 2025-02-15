#!/usr/bin/env python3

#2024/11/10

#RaspberryPi HAT(Akizuki)

#pigpio
#https://karaage.hatenadiary.jp/entry/2017/02/10/073000

#vim 関係
#https://qiita.com/kazu_death/items/46ce84f112779b2d1fb5

#python文法
#https://www.curict.com/item/65/65718fb.html#google_vignette

#python ロジック演算
#https://note.nkmk.me/python-bit-operation/

#raspi io RPi.GPIOとpigpioの比較
#https://kurafuto.org/rpigpio-pigpio/


#ソフトウェアＰＷＭ
#https://qiita.com/M_Study/items/bea2dfdd8792eb4e979f

#上よりも少し詳しいソフトウエアＰＷＭ
#https://l-w-i.net/t/raspbian/pigpio_002.txt

#RPi.GPIOによるハードウェアＰＷＭ　pigpioにあらず
#https://qiita.com/tanutanup/items/39b339c9575cf2f551d4

#キーボード割り込み　詳細
#https://qiita.com/BlueSilverCat/items/f38ba6a13cfdc9f5c56f#except-keyboardinterrupt

import pigpio
import time


LED_RED=17
LED_YLW=27
LED_GRN=22
BZ=23
SW1=24
SW2=21
LCD_BKLGT=26
PS1=26
#I2C_1
PWM_1=18
PWM_2=12

led_state=False

LEDs=[LED_RED, LED_YLW, LED_GRN]
pi=pigpio.pi()
pi.set_mode(LED_RED, pigpio.OUTPUT)
pi.set_mode(LED_YLW, pigpio.OUTPUT)
pi.set_mode(LED_GRN, pigpio.OUTPUT)

pi.set_mode(LCD_BKLGT, pigpio.OUTPUT)
#pi.write(LCD_BKLGT,1)
pi.set_PWM_frequency(LCD_BKLGT,100)
pi.set_PWM_range(LCD_BKLGT,255)

#for i in range(10):
    
    # pi.write(LED_RED, 1)
    # time.sleep(1)
    # pi.write(LED_RED,0)
    # time.sleep(1)

try:
    
    i=0
    while(True):
        pi.write(LEDs[i], int(led_state))
        print(i,LEDs[i])
        led_state=not led_state
        pi.set_PWM_dutycycle(LCD_BKLGT,(i+1)*int(255.0/3))
    
        time.sleep(0.3)
        if(i>=len(LEDs)-1):
            i=0
        else:
            i=i+1
except KeyboardInterrupt:
    pass