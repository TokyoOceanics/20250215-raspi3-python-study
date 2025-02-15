#!/usr/bin/env python3
#
from sys import argv

A=1
B=2

print(argv[0])

if len(argv)>1:
    A=int(argv[1])
    
if len(argv)>2:
    B=int(argv[2])
    
print(A,'+',B,'=',A+B)
print(A,'-',B,'=',A-B)
print(A,'*',B,'=',A*B)
print(A,'/',B,'=',A/B)
print(A,'%',B,'=',A%B)
