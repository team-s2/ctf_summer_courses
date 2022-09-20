#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from Crypto.Cipher import AES
from binascii import unhexlify, hexlify
import signal
from secret import flag
import random
import string
import hashlib

def proof_of_work():
    proof = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(20)])
    digest = hashlib.sha256(proof.encode()).hexdigest()
    print("sha256(XXXX+%s) == %s" % (proof[4:], digest))
    x = input("Give me XXXX: ")
    if len(x)!=4 or hashlib.sha256((x+proof[4:]).encode()).hexdigest() != digest: 
        print("Sorry~ bye~")
        return False
    print("Right!")
    return True

KEY = os.urandom(16)
SECRET = os.urandom(19)

def pad(msg):
    return msg + bytes([16 - len(msg) % 16] * (16 - len(msg) % 16)) 

def encrypt(msg):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(msg))


def encrypt_with_secret():
    msg = unhexlify(input("your msg: "))
    assert len(msg) <= 48
    return hexlify(encrypt(msg + SECRET)).decode()

def check():
    guess = unhexlify(input('Tell me your answer: '))
    if guess == SECRET:
        print(f"Congratulation, your're right! Here is flag: {flag}")
    else:
        print("Sorry, wrong~")


def main():
    signal.alarm(300)
    
    if not proof_of_work():
        return
    
    signal.alarm(300)
    
    for _ in range(0xBBB):
        try:
            op = input("your option: ")
            if op=='1':
                print(encrypt_with_secret())
            elif op=='2':
                check()
        except:
            exit(0)

if __name__ == '__main__':
    main()
