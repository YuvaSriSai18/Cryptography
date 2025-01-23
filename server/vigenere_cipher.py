import string
# Encryption

def generate_key_string(msg, key):
    if not msg or not key:
        raise ValueError("Both message and key must be non-empty strings.")
    
    key = list(key)
    while len(key) < len(msg):
        key.extend(key[:len(msg) - len(key)])
    
    return "".join(key[:len(msg)])

# print(generate_key_string('ab', 'eng'))  # Output: "en"
def convert_from_ascii_to_decimal(letter1, letter2):
    a = ord(letter1) - 97
    b = ord(letter2) - 97
    return (a + b ) % 26

def encrypt_data(string , key_string):
    str_arr = []
    for letter in string :
        str_arr.append(letter)
    key_str_arr = []
    for letter in key_string:
        key_str_arr.append(letter)
    Cipher_arr = []
    for i in range(len(string)):
        num = convert_from_ascii_to_decimal(str_arr[i] , key_str_arr[i])
        Cipher_arr.append(int(num + 97))
    Cipher_arr_2 = []
    for i in range(len(Cipher_arr)):
        Cipher_arr_2.append(chr(Cipher_arr[i]))
    return ''.join(Cipher_arr_2)
        
    
# encrypt_data('yuva sai')

# a = str(input('Enter a String : '))
# a_lower = a.lower()
# key = 'eng'
# key_string = generate_key_string(a_lower , key)

# print(encrypt_data(a_lower , key_string))


# Decryption

def convert_from_ascii_to_decimal_decrypt(letter1, letter2):
    a = ord(letter1) - 97
    b = ord(letter2) - 97
    return (a - b + 26) % 26  

def decrypt_data(cipher_text, key_string):
    PlainText_arr = []
    for i in range(len(cipher_text)):
        num = convert_from_ascii_to_decimal_decrypt(cipher_text[i], key_string[i])
        PlainText_arr.append(chr(num + 97)) 
    return ''.join(PlainText_arr)