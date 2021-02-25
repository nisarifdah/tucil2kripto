# Return lsfr from key in binary
def getLsfr(k):
    if(len(k)<=32): # Key is shorter than 32 characters (256 bits)
        key = extendKey(k)
    else: # Key is longer than 32 characters (256 bits) 
        key = reduceKey(k)

    binary = ''.join(format(i, '08b') for i in key)
    l = len(binary)
    output = []
    for i in range(l):
        output.append(binary[l-1])
        binary = str(int(binary[0]) ^ int(binary[l-1])) + binary[0:l-1]
    return output

# Key is shorter than 32 characters (256 bits) 
def extendKey(k):
    key = list(k)
    for i in range(len(key)):
        key[i] = ord(key[i])
    for i in range(32 - len(key)): # 32 characters for KSA
        key.append(key[i % len(key)])
    return key

# Key is longer than 32 characters (256 bits) 
def reduceKey(k):
    key = list(k)
    key_length = len(key)
    output = []
    for i in range(32):
        groupKey = key[i::32]
        output.append(xorKey(groupKey, len(groupKey)))
    return output

def xorKey(arr, n): 
    xor = 0
    for i in range(n): 
        xor ^= ord(arr[i])
    return xor 
