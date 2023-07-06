from random import randrange

text_list = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'

key = [randrange(1, 97) for _ in range(randrange(15, 30))]

print('key = ' + str(key))

def encrypt(s, k):
    out = ''
    for i in range(len(s)):
        index = text_list.index(s[i])
        index *= k[i % len(k)]
        index %= 97
        out += text_list[index]
    return out

plain = open('plain.txt', 'r').read() # TOEFL reading passage
cipher = encrypt(plain, key)
open('cipher.txt', 'w').write(cipher)