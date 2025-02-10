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

def encrypt_text():
    input_text = input("Enter a string to encrypt: ")
    key = token_bytes(16)
    key = list(key)

    cipher_text = rc4_encrypt_decrypt(input_text, key)
    
    with open("./Lab_2_4/EncryptedText.txt", "w", encoding="utf-8") as enc_file:
        enc_file.write(cipher_text)
    
    decrypted_text = rc4_encrypt_decrypt(cipher_text, key)
    
    with open("./Lab_2_4/DecryptedText.txt", "w", encoding="utf-8") as dec_file:
        dec_file.write(decrypted_text)
    
    print("Encryption & Decryption completed! Check 'EncryptedText.txt' & 'DecryptedText.txt'.")

def encrypt_file():
    filename = input("Enter filename (with extension) to encrypt: ")
    
    try:
        with open(f'./Lab_2_4/{filename}', "r", encoding="utf-8") as file:
            file_data = file.read()
        
        key = token_bytes(16)
        key = list(key)

        encrypted_data = rc4_encrypt_decrypt(file_data, key)
        
        with open("./Lab_2_4/EncryptedFile.txt", "w", encoding="utf-8") as enc_file:
            enc_file.write(encrypted_data)

        decrypted_data = rc4_encrypt_decrypt(encrypted_data, key)

        with open("./Lab_2_4/DecryptedFile.txt", "w", encoding="utf-8") as dec_file:
            dec_file.write(decrypted_data)

        print("Encryption & Decryption completed! Check 'EncryptedFile.txt' & 'DecryptedFile.txt'.")

    except FileNotFoundError:
        print("Error: File not found!")

print("1. Encrypt a text message")
print("2. Encrypt a file")

choice = input("Choose an option: ")

if choice == "1":
    encrypt_text()
elif choice == "2":
    encrypt_file()
else:
    print("Invalid choice. Please select 1 or 2.")
