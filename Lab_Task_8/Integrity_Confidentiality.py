import hashlib
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# --- Step 1: Diffie-Hellman Key Exchange (Simplified) ---
def diffie_hellman_key_exchange():
    private_key = int.from_bytes(get_random_bytes(16), "big")  # Private key (random)
    public_base = 5  # Common base
    public_modulus = 23  # Common prime modulus
    public_key = pow(public_base, private_key, public_modulus)  # Public key
    return private_key, public_key, public_modulus

# --- Step 2: Compute Shared Secret ---
def compute_shared_secret(private_key, public_key, public_modulus):
    return pow(public_key, private_key, public_modulus).to_bytes(16, 'big')  # Shared secret

# --- Step 3: Hashing the Message ---
def compute_sha256_hash(message):
    return hashlib.sha256(message.encode()).digest()  # SHA-256 hash

# --- Step 4: Encrypt Message + Hash using AES ---
def encrypt_message(session_key, message):
    hash_code = compute_sha256_hash(message)
    combined_data = message.encode() + hash_code  # Append hash to message
    cipher = AES.new(session_key, AES.MODE_CBC)  # AES in CBC mode
    ciphertext = cipher.encrypt(pad(combined_data, AES.block_size))  # Encrypt padded message
    return cipher.iv, ciphertext

# --- Step 5: Decrypt and Verify Integrity ---
def decrypt_and_verify(session_key, iv, ciphertext):
    cipher = AES.new(session_key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)  # Decrypt
    message, received_hash = decrypted_data[:-32], decrypted_data[-32:]  # Extract message and hash
    computed_hash = compute_sha256_hash(message.decode())  # Compute hash of message
    if received_hash == computed_hash:
        print("✅ Integrity Verified! Message:", message.decode())
    else:
        print("❌ Integrity Check Failed! Message has been tampered.")

# --- Simulation of Secure Communication ---
private_key_sender, public_key_sender, modulus = diffie_hellman_key_exchange()
private_key_receiver, public_key_receiver, _ = diffie_hellman_key_exchange()

# Compute shared session key (Both sides should get the same key)
session_key_sender = compute_shared_secret(private_key_sender, public_key_receiver, modulus)
session_key_receiver = compute_shared_secret(private_key_receiver, public_key_sender, modulus)

# Message to send
message = "This is a confidential message."

# Sender encrypts message
iv, ciphertext = encrypt_message(session_key_sender, message)

# Receiver decrypts and verifies integrity
decrypt_and_verify(session_key_receiver, iv, ciphertext)
