import string

letters = list(string.ascii_uppercase) 
# print(letters)
cipher_list = ['A', 'N', 'D', 'R', 'E', 'W', 'I', 'C', 'K', 'S', 'O', 'H', 'T', 
               'B', 'F', 'G', 'J', 'L', 'M', 'P', 'Q', 'U', 'V', 'X', 'Y', 'Z']

cipher_text = 'SEEMSEAOMEDSAMHL'
plain_text = ''
for i in cipher_text:
    if i in letters:
        idx = letters.index(i)
        plain_text += cipher_list[idx]
    else:
        plain_text += i

print(plain_text) # MEETMEAFTERMATCH