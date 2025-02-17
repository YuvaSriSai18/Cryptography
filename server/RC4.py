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

def rc4_encrypt_decrypt(text, key):
    S = KSA(key)
    key_stream = PRGA(S, len(text))
    result = ''.join(chr(ord(text[i]) ^ key_stream[i]) for i in range(len(text)))
    return result

def encrypt_text(input_text):
    key = token_bytes(16)
    key = list(key)

    cipher_text = rc4_encrypt_decrypt(input_text, key)
    
    decrypted_text = rc4_encrypt_decrypt(cipher_text, key)
    
    return cipher_text , decrypted_text

def encrypt_file(file_data):
    key = token_bytes(16)
    key = list(key)

    encrypted_data = rc4_encrypt_decrypt(file_data, key)
        
    decrypted_data = rc4_encrypt_decrypt(encrypted_data, key)
    
    return encrypted_data , decrypted_data