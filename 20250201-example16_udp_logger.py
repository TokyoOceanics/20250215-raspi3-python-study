#!/usr/bin/env python3

import socket
import datetime

print('Listening UDP port', 1024,'...',flush=True)

try:
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind(("",1024))
except Exception as e:
    print(e)
    exit()

while sock:
    udp=sock.recv(64)
    udp=udp.decode()
    udp=udp.strip()
    if udp.isprintable():
        date=datetime.datetime.today()
        print(date.strftime("%Y/%m/%d %H:%M"), end="")
        print(", "+udp, flush=True)
        