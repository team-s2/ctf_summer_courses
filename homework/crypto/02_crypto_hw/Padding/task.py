#!/usr/bin/env python3

from binascii import hexlify, unhexlify
import os, base64, time, random, string
from Crypto.Cipher import AES
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

key = os.urandom(16)
iv = os.urandom(16)

def unpad(msg: bytes):
    if bytes([msg[-1]]) * msg[-1] != msg[-msg[-1]:]:
        return b"padding error!?"
    return msg[:-msg[-1]]

def decrypt(iv:bytes, msg: bytes):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(msg)
    decrypted = unpad(decrypted)
    return decrypted


if __name__ == '__main__':
    signal.alarm(300)
    if not proof_of_work():
        exit(0)
    signal.alarm(300)
    while True:
        try:
            cipher = unhexlify(input("your cipher: "))
            assert len(cipher) % 16 == 0, "len error!"
            msg = decrypt(cipher[:16], cipher[16:])
            if msg==b'This is an arbitrary plaintext':
                print(f"Congratulation, you got it! Here is the flag: {flag}")
            else:
                print(hexlify(msg).decode())
        except:
            exit(0)