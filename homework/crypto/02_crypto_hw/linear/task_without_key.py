from secret import key_4bytes

sbox = [62, 117, 195, 179, 20, 210, 41, 66, 116, 178, 152, 143, 75, 105, 254, 1, 158, 95, 101, 175, 191, 166, 36, 24, 50, 39, 190, 120, 52, 242, 182, 185, 61, 225, 140, 38, 150, 80, 19, 109, 246, 252, 40, 13, 65, 236, 124, 186, 214, 86, 235, 100, 97, 49, 197, 154, 176, 199, 253, 69, 88, 112, 139, 77, 184, 45, 133, 104, 15, 54, 177, 244, 160, 169, 82, 148, 73, 30, 229, 35, 79, 137, 157, 180, 248, 163, 241, 231, 81, 94, 165, 9, 162, 233, 18, 85, 217, 84, 7, 55, 63, 171, 56, 118, 237, 132, 136, 22, 90, 221, 103, 161, 205, 11, 255, 14, 122, 47, 71, 201, 99, 220, 83, 74, 173, 76, 144, 16, 155, 126, 60, 96, 44, 234, 17, 215, 107, 138, 159, 183, 251, 3, 198, 0, 89, 170, 131, 151, 219, 29, 230, 32, 187, 125, 134, 64, 12, 202, 164, 247, 25, 223, 222, 119, 174, 67, 147, 146, 206, 51, 243, 53, 121, 239, 68, 130, 70, 203, 211, 111, 108, 113, 8, 106, 57, 240, 21, 93, 142, 238, 167, 5, 128, 72, 189, 192, 193, 92, 10, 204, 87, 145, 188, 172, 224, 226, 207, 27, 218, 48, 33, 28, 123, 6, 37, 59, 4, 102, 114, 91, 23, 209, 34, 42, 2, 196, 141, 208, 181, 245, 43, 78, 213, 216, 232, 46, 98, 26, 212, 58, 115, 194, 200, 129, 227, 249, 127, 149, 135, 228, 31, 153, 250, 156, 168, 110]
ptable = [
    0, 4, 8, 12, 
    1, 5, 9, 13, 
    2, 6, 10, 14, 
    3, 7, 11, 15, 
    16, 20, 24, 28,
    17, 21, 25, 29,
    18, 22, 26, 30,
    19, 23, 27, 31,
]

def s2b(s):
    return [int(x) for x in bin(int.from_bytes(s,'big'))[2:].zfill(32)]

def b2s(b):
    return bytes.fromhex(hex(int("".join([str(x) for x in b]), 2))[2:].zfill(8))


def permutation(a):
    assert len(a) == 4
    bits = s2b(a)
    bits = [bits[ptable[i]] for i in range(32)]
    return b2s(bits)

def substitute(a):
    return bytearray(sbox[i] for i in a)

def xor(a, b):
    assert len(a) == len(b)
    return bytes([x^y for x,y in zip(a,b)])

class ASPN(object):

    def __init__(self, key, key_size=4, rounds=4):
        assert len(key) == key_size
        self.key = key
        self.key_size = key_size
        self.rounds = rounds
        self.key_schedule()

    def key_schedule(self):
        self.roundkey = self.key
        for i in range(6):
            tmp = [self.roundkey[-3], self.roundkey[-1]]
            tmp = [sbox[tmp[0]], sbox[tmp[1]]]
            tmp = [tmp[0]^self.roundkey[-4], tmp[1]^self.roundkey[-2]]
            self.roundkey = self.roundkey + bytes(tmp)
        print(list(self.roundkey))

    def get_roundkey(self, k):
        return self.roundkey[k*4:(k+1)*4]

    def encrypt(self, plain):
        assert len(plain) == 4
        block = plain
        for i in range(self.rounds-1):
            block = xor(block, self.get_roundkey(i))
            block = substitute(block)
            if i != self.rounds-2:
                # Permutation in the last round is of no purpose.
                block = permutation(block)
        block = xor(block, self.get_roundkey(i+1))
        return block


import os

key = key_4bytes

aspn = ASPN(key)


res = b""
for i in range(pow(2,16)):
    print(i)
    plain = os.urandom(4)
    cipher = aspn.encrypt(plain)
    res += plain+cipher

with open("data", "wb") as f:
    f.write(res)