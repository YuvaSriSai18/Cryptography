from sympy import isprime, mod_inverse
import math
import random

def generate_Key(p, q):
    # Ensure p and q are prime numbers
    if not (isprime(p) and isprime(q)):
        raise ValueError("Both p and q must be prime numbers.")

    print("Entered correct values")

    # Compute n and Euler's totient (phi)
    n = p * q
    print(f'n value : {n}')
    pi = (p - 1) * (q - 1)
    print(f'pi value : {pi}')

    # Select a suitable e value
    def set_e_value(pi):
        possible_e = [i for i in range(2, pi) if math.gcd(pi, i) == 1]
        return random.choice(possible_e) if possible_e else None

    e = set_e_value(pi)
    if e is None:
        raise ValueError("Failed to find a suitable e value.")
    
    print(f'e value : {e}')

    # Compute d as the modular inverse of e mod pi
    d = mod_inverse(e, pi)
    print(f'd value : {d}')

    # Define public and private keys
    public_key = (e, n)
    private_key = (d, n)

    print(f'Public Key (e, n) : {public_key}')
    print(f'Private Key (d, n) : {private_key}')

    return public_key, private_key


# generate_Key(p,q)