from secrets import token_bytes

def KSA(key):
    S = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i] 
    return S

def PRGA(S, text_length):
    i = j = 0
    key_stream = []
    for _ in range(text_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i] 
        t = (S[i] + S[j]) % 256
        key_stream.append(S[t])
    return key_stream

def rc4_encrypt_decrypt(plaintext, key):
    S = KSA(key)
    key_stream = PRGA(S, len(plaintext))
    cipher_text = ''.join(chr(ord(plaintext[i]) ^ key_stream[i]) for i in range(len(plaintext)))
    return cipher_text


input_text = input("Enter a string to encrypt: ")
key = token_bytes(16)

key = list(key)

# Encrypt the text
cipher_text = rc4_encrypt_decrypt(input_text, key)
print(f"Cipher Text: {cipher_text}")

# Decrypt the text (RC4 encryption and decryption are symmetric)
decrypted_text = rc4_encrypt_decrypt(cipher_text, key)
print(f"Decrypted Text: {decrypted_text}")
