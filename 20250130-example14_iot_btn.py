#!/usr/bin/env python3

port=21
udp_to='255.255.255.255'
udp_port=1024

import socket
from gpiozero import Button
from time import sleep
from sys import argv

print(argv[0])
if(len(argv)>2):
    port=int(argv[1])

btn=Button(port, bounce_time=0.1,pull_up=True)

b=1
while True:
    try:
        while(b==btn.value):
            sleep(0.1)
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt")
        btn.close()
        exit()

    b=int(not(b))
    if b==0:
        udp_s='Ping'
    else:
        udp_s='Pong'
    print('GPIO'+str(port)+'=',b,udp_s)

    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    udp_bytes=(udp_s+'\n').encode()
    try:
        sock.sendto(udp_bytes, (udp_to,udp_port))
    except Exception as e:
        print (e)
    sock.close()



