from Key_Generation import generate_Key

# Get prime numbers from user
p = int(input('Enter prime number p: '))
q = int(input('Enter prime number q: '))

# Generate keys
public_key, private_key = generate_Key(p, q)

## Encryption
def encrypt():
    e, n = public_key
    plaintext = input('Enter Plain Text (< n): ')

    # Convert text to an integer using UTF-8 encoding
    M = int.from_bytes(plaintext.encode(), 'big')

    if M >= n:
        raise ValueError("Message must be smaller than n.")
    
    print(f'M value : {M}')
    
    # Encrypt message: C = M^e mod n
    c = pow(M, e, n)
    return c 

# Encrypt message
cipherText = encrypt()
print(f'Encrypted Cipher: {cipherText}')

## Decryption
def decrypt(c):
    d, n = private_key

    # Decrypt: M = C^d mod n
    M = pow(c, d, n)

    # Convert decrypted integer back to string
    try:
        decrypted_text = M.to_bytes((M.bit_length() + 7) // 8, 'big').decode()
    except:
        decrypted_text = str(M)  # Fallback if decoding fails

    return decrypted_text

# Decrypt the cipherText
print(f'Decrypted Message: {decrypt(cipherText)}')
