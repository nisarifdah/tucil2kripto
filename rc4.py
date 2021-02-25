import binascii
import codecs
from lsfr import *

def convert_text(s):
    return ([ord(c) for c in s])

def ksa(key):
    cKey = convert_text(key)
    cKey_length = len(cKey)
    
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + cKey[i % cKey_length]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def ksa1(key):
    ksaKey = ksa(key)
    ksaKey_length = len(ksaKey)
    key_length = len(key)

    lsfr = getLsfr(key)
    
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + ksaKey[i % ksaKey_length] + int(ord(key[i % key_length])) + int(lsfr[i])) % 256
        S[i], S[j] = S[j], S[i]

    return S


def prga(x):
    i = 0
    j = 0
    
    while True:
        i = (i + 1) % 256
        j = (j + x[i]) % 256
        x[i], x[j] = x[j], x[i]
        result = x[(x[i] + x[j]) % 256]
        yield result
    
def getkey(key):
    a = ksa1(key)
    return prga(a)

def encrypt(key, text):
    #key = convert_text(key)
    t = convert_text(text)
    k = getkey(key)

    result = []
    for i in t:
        r = ("%02X" % (i ^ next(k)))
        result.append(r)
    hasil = ''.join(result)
    return (codecs.decode(hasil, 'hex_codec').decode('latin-1'))
    #return hasil

def decrypt(key, text):
    t = convert_text(text)
    #key = convert_text(key)
    k = getkey(key)

    result = []
    for i in t:
        r = ("%02X" % (i ^ next(k)))
        result.append(r)
    hasil = ''.join(result)
    return(codecs.decode(hasil, 'hex_codec').decode('latin-1'))

#a = encrypt('123','world')
#print(a)
#A6 11 24 62 D2
