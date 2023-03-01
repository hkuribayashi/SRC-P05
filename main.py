def KSA(key):
    s = [i for i in range(256)]
    j = 0
    for i in range(256):
        index = i % len(key)
        caracter = key[index]
        k = ord(caracter)
        k = ord(key[i % len(key)])
        j = (j + s[i] + k) % 256
        s[i], s[j] = s[j], s[i]
    return s


def PRGA(s, amount):
    j = 0
    k = []
    for i in range(amount):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        k.append(s[(s[i] + s[j]) % 256])
    return k


def XOR(pt, k):
    ct = []
    for i in range(len(pt)):
        ct.append(ord(pt[i]) ^ k[i])
    return ct


def RC4(plaintext, key):
    s = KSA(key)
    k = PRGA(s, len(plaintext))
    ct = XOR(plaintext, k)
    return ct


cifra = RC4("hugo", "123456")
print(cifra)
