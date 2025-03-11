from Crypto.Cipher import AES
import hashlib
import os
import base64
# Encryption function
def diffie_encrypt_message(plain_text, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(plain_text.encode())
    return base64.b64encode(nonce + ciphertext).decode()  # Convert to Base64 for JSON transfer

# Decryption function
def diffie_decrypt_message(cipher_text, key):
    cipher_data = base64.b64decode(cipher_text)
    nonce = cipher_data[:16]  # First 16 bytes are nonce
    ciphertext = cipher_data[16:]
    
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext).decode()

# Example Usage
# shared_secret = 123456  # Simulated shared secret from Diffie-Hellman
# aes_key = hashlib.sha256(str(shared_secret).encode()).digest()  # Convert to AES key

# message = "Hello, this is a secure message!"
# encrypted_msg = encrypt_message(message, aes_key)
# print(f"Encrypted: {encrypted_msg}")

# decrypted_msg = decrypt_message(encrypted_msg, aes_key)
# print(f"Decrypted: {decrypted_msg}")
