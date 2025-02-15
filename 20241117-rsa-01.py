#!/usr/bin/env python3

from gmpy2 import mpz, powmod, gcdext

def genkey(p, q, e=65537):
    n=p*q
    m=(p-1)*(q-1)
    
    _, d, _=gcdext(e,m)
    
    while d<0:
        d+=m
    
    return (n, e), (n, int(d))
    
def encrypt(v, pubkey):
    return list(map(lambda v: int(powmod(v, pubkey[1], pubkey[0])),v))

def decrypt( v, pubkey):
    return list(map(lambda v: int(powmod(v, prvkey[1], prvkey[0])),v))


pubkey, prvkey=genkey(3,11,e=3)

a=[13]
b=encrypt(a, pubkey)

adash=decrypt(b, prvkey)

print(f'公開鍵={pubkey} 秘密鍵={prvkey}, 平文={a}, 暗号文={b}, 復号={adash}')

    
    