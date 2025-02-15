#!/usr/bin/env python3

port_R=17
port_G=27
port_Y=22
#ports=[port_R,port_G,port_Y]
pin_numbers = [port_R, port_Y, port_G]  # 使用するGPIOピン

colors=['off','red','rgn','ylw','ble','red-purple','ble-grn','wht']
color=colors.index('wht')
leds=[]

from wsgiref.simple_server import make_server
from gpiozero import LED





def setup_leds():
    global leds  # グローバル変数を明示的に使用
    leds = [LED(pin) for pin in pin_numbers ]

"""
#ダメなコード
def close_leds():
    global leds
    for pin in len(leds):
        leds[pin].close()
"""

#chatGPT推奨のコード
def close_leds():
    global leds
    for led in leds:
        led.close()



        

def wsgi_app(environ, start_response):
    global color
    color=colors.index('wht')
    query=environ.get('QUERY_STRING')
    sp=query.find("=")
    if sp>=0 and sp+1<len(query):
       if query[sp+1:].isdigit():
           color=int(query[sp+1:]) 
           color %= len(colors)
    print("Color=", color, colors[color])
    
    #print("pin_nubmers",pin_numbers) 
    #print("pin_nubmers length=",len(pin_numbers)) 
    
    
    for i in range(len(pin_numbers)):
        print("[",str(i),"]")
        port=pin_numbers[i]
        print("[",str(port),"]")
        b=(color>>i)&1
        print("GPIO"+str(port),"=",b)
        leds[i].value=b
        
    ok='Color='+str(color)+" ("+colors[color]+")\r\n"
    #print("ok=",str(ok))
    ok=ok.encode("utf-8")
    start_response("200 OK", [("Content-type","text/plain; charset=utf-8")])
    return [ok ]
   
index=0    
setup_leds()
    
try:
    httpd=make_server("",80,wsgi_app)
    print("http port 80")
    
except PermissionError:
    httpd=make_server("",8080,wsgi_app)
    print("HTTP port 8080")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nKeyboard Interrupt")
    close_leds()
    exit()
    
    
    
    
        