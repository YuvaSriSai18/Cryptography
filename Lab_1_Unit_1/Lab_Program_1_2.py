def encrypt(plain_text,shift_num):
    result = ""

    for i in range(len(plain_text)):
        char = plain_text[i]
        
        if (char.isupper()):
            result += chr((ord(char) + shift_num -65) % 26 + 65)
        else:
            result += chr((ord(char) + shift_num - 97) % 26 + 97)

    return result


print(encrypt('computerscienceengineeringsrmuniversity' , 4))