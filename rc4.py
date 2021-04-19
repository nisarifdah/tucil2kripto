import binascii
import codecs
from lsfr import *

def convert(s): # Convert string to ASCII
    return ([ord(c) for c in s])

def ksa(key):
    cKey = convert(key)
    cKey_length = len(cKey)
    
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + cKey[i % cKey_length]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def ksa_complex(key):
    lsfr = getLsfr(key)
    key_length = len(key)
    ksaKey = ksa(key)
    ksaKey_length = len(ksaKey)

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


def execute(key, text, mode): # Encrypt or decrypt
    if(mode == '1'): #input text
        t = convert(text)
    else: #file
        t = text
    k = prga(ksa_complex(key))

    result = []
    for i in t:
        r = ("%02X" % (i ^ next(k)))    # i xor k, format in 2-digit hex
        result.append(r)
    hasil = ''.join(result)
    return (codecs.decode(hasil, 'hex_codec').decode('latin-1'))
