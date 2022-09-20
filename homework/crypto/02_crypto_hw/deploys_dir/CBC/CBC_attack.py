# coding: utf-8

from Crypto.Cipher import AES
from binascii import hexlify, unhexlify

def padding(m):
    # 填充到8字节对齐,如m='1111111111',则填充后变为'1111111111\x06\x06\x06\x06\x06\x06'
    return m + (16 - len(m)%16) * bytes([16 - len(m)%16])

key = b'1234567812345678'
IV = b'ABCDEFGHABCDEFGH'

aes = AES.new(key, AES.MODE_CBC, IV)
message = b'1'*16 + b'2'*16 + b'1'*15 + b'0'
enc = aes.encrypt(padding(message))
enc_hex = hexlify(enc)

print(enc_hex)
for i in range(0, len(enc_hex), 32):
    print(enc_hex[i:i+32])

'''
f40a6ea520e726ec098158d392082cf1c082d2336648561781b39542b41e2df195296f3f7de6b92dd643a1ce57bdda3924b8af51101d29f7d3662ac1128571bc
f40a6ea520e726ec098158d392082cf1 = encrypt(plain_A ^ IV) = cipher_A
c082d2336648561781b39542b41e2df1 = encrypt(cipher_A ^ plian_B) = cipher_B
95296f3f7de6b92dd643a1ce57bdda39 = encrypt(cipher_B ^ plian_C) = cipher_C
24b8af51101d29f7d3662ac1128571bc = encrypt(cipher_C ^ plian_D) = cipher_D
'''

aes = AES.new(key, AES.MODE_CBC, IV)
m = aes.decrypt(enc)
print(m)


# 修改其中一个字节,使第三个明文块变为'1'*16
enc_t = enc[:16+16-1] + bytes([enc[16+16-1] ^ 1]) + enc[32:] 
aes = AES.new(key, AES.MODE_CBC, IV)
m = aes.decrypt(enc_t)
print(m)
# 31313131313131313131313131313131 9d812621db606e30b33e8919c7e22d6a 31313131313131313131313131313131 10101010101010101010101010101010