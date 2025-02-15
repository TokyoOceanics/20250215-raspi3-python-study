#!/usr/bin/env python3

def add_and_sub(a, b):
    return a+b, a-b

x=10
y=20

u, v=add_and_sub(x,y)
print('a+b=',u, 'a-b=',v)