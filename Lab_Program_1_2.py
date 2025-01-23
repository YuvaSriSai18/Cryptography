def encrypt(plain_text,shift_num):
    result = ""

    for i in range(len(plain_text)):
        char = plain_text[i]
        
        if (char.isupper()):
            result += chr((ord(char) + shift_num -65) % 26 + 65)
        else:
            result += chr((ord(char) + shift_num - 97) % 26 + 97)

    return result

def decrypt(cipher_text, shift_num):
    result = ""

    for i in range(len(cipher_text)):
        char = cipher_text[i]

        if char.isupper():  # For uppercase characters
            result += chr((ord(char) - shift_num - 65) % 26 + 65)
        elif char.islower():  # For lowercase characters
            result += chr((ord(char) - shift_num - 97) % 26 + 97)
        else:  # Non-alphabetic characters remain unchanged
            result += char

    return result



print(encrypt('computerscienceengineeringsrmuniversity' , 4))
# print(decrypt('gsqtyxivwgmirgiirkmriivmrkwvqyrmzivwmxc' , 4))
print('\n')
for i in range(20):
    print(f'Decrypted Text of Key {i + 1} : {decrypt('PHHW PH DIWHU WKH WRJD SDUWB' , i + 1)}')