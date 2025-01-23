import string
import random

lowercase = list(string.ascii_lowercase)  
cipher_list = list(string.ascii_uppercase) 
random.shuffle(cipher_list) 

print("Lowercase:", lowercase)
print("Cipher List:", cipher_list)

plain_text = 'yu va'
cipher_text = ''
plain_text = plain_text.lower()  

for i in plain_text:
    if i in lowercase:
        idx = lowercase.index(i)  
        cipher_text += cipher_list[idx] 
    else:
        cipher_text += i  

print("Plain Text:", plain_text)
print("Cipher Text:", cipher_text)
