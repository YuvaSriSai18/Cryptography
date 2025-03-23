from ecdsa import NIST384p, ellipticcurve
import os

# Function to generate a private key (random 32-byte integer)
def generate_private_key():
    return int.from_bytes(os.urandom(32), byteorder='big')

# Function to generate a public key from a private key
def generate_public_key(private_key, generator):
    return generator * private_key  # ECC multiplication

# Function to perform ECC key exchange
def key_exchange(private_key_a, private_key_b, generator):
    public_key_a = generate_public_key(private_key_a, generator)
    public_key_b = generate_public_key(private_key_b, generator)

    # Compute shared secrets
    shared_secret_a = public_key_b * private_key_a
    shared_secret_b = public_key_a * private_key_b

    assert shared_secret_a == shared_secret_b, "Shared secrets do not match!"

    return shared_secret_a

# Example Usage
generator = NIST384p.generator  # ECC generator
private_key_a = generate_private_key()
private_key_b = generate_private_key()

shared_secret = key_exchange(private_key_a, private_key_b, generator)
print(f"Shared Secret: {shared_secret.x()}")  # Print only the x-coordinate
