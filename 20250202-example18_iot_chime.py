#!/usr/bin/env

port=23
ping_f=554
pong_f=440

from wsgiref.simple_server import make_server
from gpiozero import TonalBuzzer
from time import sleep
from sys import argv
import threading

def chime():
    global buz 
    buz.play(ping_f)
    sleep(0.25)
    buz.play(pong_f)
    sleep(0.3)
    buz.stop()

def wsgi_app(environ, start_response):
    thread=threading.Thread(target=chime)
    thread.start()
    ok="OK\r\n"
    ok=ok.encode()
    start_response("200 OK", [("Content-type","text/playn; charset=utf-8")])
    return [ok]

print(argv[0])
if len(argv)>=2:
    port=int(argv[1])
buz=TonalBuzzer(port,initial_value=1.0)
buz.stop()

try:
    httpd=make_server("",80, wsgi_app)
    print("HTTP port 80")
except PermissionError:
    httpd=make_server("",8080,wsgi_app)
    print("HTTP port 8080")
    
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nKeyboardInterrupt")
    buz.close()
    exit()
    
