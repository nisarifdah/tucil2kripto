import binascii
import codecs

def convert_text(s):
    return ([ord(c) for c in s])

def ksa(key):
    a = 256
    key_length = len(key)
    
    S = list(range(256))
    j = 0
    for i in range(a):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def ksa1(k):
    key = ksa(k)
    a = 256
    key_length = len(key)
    k_length = len(k)
    
    S = list(range(256))
    j = 0
    for i in range(a):
        j = (j + S[i] + key[i % key_length] + k[i % k_length]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def prga(x):
    i = 0
    j = 0
    
    while True:
        i = (i + 1) % 256
        j = (j + x[i]) % 256
        x[i] = x[j]
        x[j] = x[i]
        result = x[(x[i] + x[j]) % 256]
        yield result
    
def getkey(key):
    a = ksa(key)
    return prga(a)

def encrypt(key, text):
    key = convert_text(key)
    t = convert_text(text)
    k = getkey(key)

    result = []
    for i in t:
        r = ("%02X" % (i ^ next(k)))
        result.append(r)
    return ''.join(result)

def decrypt(key, text):
    t = binascii.unhexlify(text)
    key = convert_text(key)
    k = getkey(key)

    result = []
    for i in t:
        r = ("%02X" % (i ^ next(k)))
        result.append(r)
    hasil = ''.join(result)
    return(codecs.decode(hasil, 'hex_codec').decode('utf-8'))


    
