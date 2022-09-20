#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from Crypto.Cipher import AES
from binascii import unhexlify, hexlify
import signal

from secret import part_flag, full_flag
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
IV = os.urandom(16)
SECRET = os.urandom(22)

def pad(msg):
    return msg + bytes([16 - len(msg) % 16] * (16 - len(msg) % 16)) 

def unpad(msg):
	return msg[: -msg[-1]]

def encrypt(iv, msg):
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(pad(msg))


def encrypt_with_secret():
    msg = unhexlify(input("your msg: "))
    assert len(msg) <= 16
    return hexlify(encrypt(IV, msg + SECRET)).decode()

def decrypt(iv, msg):
	cipher = AES.new(KEY, AES.MODE_CBC, iv)
	return unpad(cipher.decrypt(msg))

def check():
    guess = unhexlify(input('Tell me your answer: '))
    if len(guess) >= 15:
        if guess[:15] == SECRET[:15]:
            print(f"Well done, the part flag: {part_flag}")
    if guess == SECRET:
        print(f"Congratulation, your're right! Here is the full flag: {full_flag}")
    else:
        print("Sorry, wrong~")

def welcome():
    return hexlify(encrypt(IV, b'This\'s a test for CBC byte flip attack~')).decode()


def main():
    signal.alarm(300)
    if not proof_of_work():
        return
    
    signal.alarm(300)
    
    print(welcome())

    for _ in range(0xCCC):
        try:
            msg = unhexlify(input("your option: "))
            msg = decrypt(msg[:16], msg[16:])
            if msg.startswith(b"Get secret"):
                print(encrypt_with_secret())
            elif msg.startswith(b"Check"):
                check()
        except:
            exit(0)

if __name__ == "__main__":
    main()