
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
        result = (x[i] + x[j]) % 256
        streamkey = x(result)
        yield streamkey



b = convert_text('0123!klm')
c = ksa(b)
d = ksa1(b)
e = prga(d)
print(d)
print(e)