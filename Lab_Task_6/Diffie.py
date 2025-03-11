import random

def diffie_hellman(p, g):
    # Private keys chosen by A and B
    a = random.randint(2, p-2)  # Private key of A
    b = random.randint(2, p-2)  # Private key of B

    # Public keys
    A = pow(g, a, p)  # A's public key
    B = pow(g, b, p)  # B's public key

    # Shared secrets
    shared_secret_A = pow(B, a, p)  # A computes shared secret
    shared_secret_B = pow(A, b, p)  # B computes shared secret

    assert shared_secret_A == shared_secret_B  # Both should match
    return shared_secret_A


# Example values (using small primes for simplicity)
p = 23  # Large prime
g = 5   # Primitive root modulo p   

shared_secret = diffie_hellman(p, g)
print(f"Shared Secret: {shared_secret}")
