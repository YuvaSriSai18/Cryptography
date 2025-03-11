from Crypto.Cipher import AES
import hashlib
import os

# Encryption function
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return nonce + ciphertext  # Send nonce with the encrypted message

# Decryption function
def decrypt_message(encrypted_message, key):
    nonce = encrypted_message[:16]
    ciphertext = encrypted_message[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext).decode()

# Example Usage
shared_secret = 123456  # Simulated shared secret from Diffie-Hellman
aes_key = hashlib.sha256(str(shared_secret).encode()).digest()  # Convert to AES key

message = "Hello, this is a secure message!"
encrypted_msg = encrypt_message(message, aes_key)
print(f"Encrypted: {encrypted_msg}")

decrypted_msg = decrypt_message(encrypted_msg, aes_key)
print(f"Decrypted: {decrypted_msg}")
