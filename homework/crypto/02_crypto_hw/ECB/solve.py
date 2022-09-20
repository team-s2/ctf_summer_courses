from pwn import *
from binascii import hexlify

# io = remote("127.0.0.1", 13100)
io = remote("10.12.77.33", 13100)


def proof_of_work(suffix, target):
    import itertools
    import string
    import hashlib
    for comb in itertools.product(string.ascii_letters+string.digits, repeat=4):
        comb = "".join(comb)
        if hashlib.sha256(comb.encode() + suffix).hexdigest() == target.decode():
            return comb
    raise "NOT FOUND"

io.recvuntil(b"XXXX+")
known = io.recvuntil(b")")[:-1]
io.recvuntil(b"== ")
target = io.recvuntil(b"\n")[:-1]

io.sendline(proof_of_work(known, target))

known_secret = b""

for i in range(15):
    io.sendlineafter(b"your option: ", b"1")
    io.sendlineafter(b"your msg: ", hexlify(b"A"*(15-i)))
    right = io.recvuntil(b"\n")[:32]
    print(right)
    for c in range(256):
        io.sendlineafter(b"your option: ", b"1")
        io.sendlineafter(b"your msg: ", hexlify(b"A"*(15-i)+known_secret+bytes([c])))
        guess = io.recvuntil(b"\n")[:32]
        if guess == right:
            known_secret += bytes([c])
            break
    print(f"current secret: {known_secret}")
    
for i in range(4):
    io.sendlineafter(b"your option: ", b"1")
    io.sendlineafter(b"your msg: ", hexlify(b"A"*(16-i)))
    right = io.recvuntil(b"\n")[32:64]
    print(right)
    for c in range(256):
        io.sendlineafter(b"your option: ", b"1")
        io.sendlineafter(b"your msg: ", hexlify(b"A"*(16-i)+known_secret+bytes([c])))
        guess = io.recvuntil(b"\n")[32:64]
        if guess == right:
            known_secret += bytes([c])
            break
    print(f"current secret: {known_secret}")
    
io.sendlineafter(b"your option: ", b"2")
io.sendlineafter(b"your answer: ", hexlify(known_secret))

print(io.recvuntil(b"\n"))

io.close()