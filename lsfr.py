# Return lsfr from key in binary
def getLsfr(key):
    binary = ''.join(format(ord(i), '08b') for i in key)
    l = len(binary)
    output = []
    for i in range(l):
        output.append(binary[l-1])
        binary = str(int(binary[0]) ^ int(binary[l-1])) + binary[0:l-1]
    return output

# Key is shorter than 32 characters (256 bits) 
def extendKey(key):
    key = list(key)
    for i in range (32 - len(key)): # 32 characters for KSA
        key.append(key[i % len(key)])
    return ''.join(key)