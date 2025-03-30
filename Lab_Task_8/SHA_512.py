import hashlib

def generate_sha512_hash(text):
    sha512 = hashlib.sha512()
    sha512.update(text.encode('utf-8'))
    return sha512.hexdigest()

# Example Usage
text = input("Enter text to hash: ")
hash_code = generate_sha512_hash(text)
print("SHA-512 Hash:", hash_code)
