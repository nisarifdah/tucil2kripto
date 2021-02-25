def lsfr(key):
    binary = ''.join(format(ord(i), '08b') for i in key)
    l = len(binary)
    output = []
    for i in range(l):
        output.append(binary[l-1])
        binary = str(int(binary[0]) ^ int(binary[l-1])) + binary[0:l-1]
    return output
    
print(lsfr('a'))