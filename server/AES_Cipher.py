from Crypto.Cipher import AES 
from secrets import token_bytes 

key = token_bytes(16)

def aes_encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce 
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag 
def aes_decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False 

# nonce, ciphertext, tag = aes_encrypt(input("Enter a message: "))
# plaintext = aes_decrypt(nonce, ciphertext, tag)

# print(f'\n Plain Text Entered : {plaintext} \n Cipher Text in base 64 : {ciphertext} , \n nonce : {nonce} \n tag : {tag}\n')
# if not plaintext:
#     print("Message is corrupted")
# else:
#     print(f'Plain text: {plaintext}')