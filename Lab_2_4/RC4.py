def KSA():
    a = [i for i in range(256)]
    # print(a)
    j = 0
    for i in range(len(a)):
        j =( j + a[i] + a[j]) % 256
        a[i],a[j] = a[j],a[i]
        # j += 1
        
    # print(a)
    return a 
# KSA()

def PRGA(list_a):
    i = j = 0
    key = []
    for i in range(len(list_a)):
        i = (i + 1) % 256
        j = (j + list_a[i]) % 256
        list_a[i],list_a[j] = list_a[j],list_a[i]
        t = (list_a[i] + list_a[j]) % 256
        key.append(t)
    return key
a = KSA()
key = PRGA(a)
# print(key)
cipherText = ''
ip = input('Enter a string : ')
for i in range(len(ip)):
    xor = ord(ip[i]) ^ key[i]
    cipherText += chr(xor)
print(f'Cipher Text : {cipherText}')
