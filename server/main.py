from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS module
from vigenere_cipher import generate_key_string, encrypt_data, decrypt_data
from playfair import encrypt, Decrypt
from AES_Cipher import aes_decrypt , aes_encrypt
from Diffie_Hellman import diffie_encrypt_message , diffie_decrypt_message 
import hashlib , base64 , os
app = Flask(__name__)
CORS(app,resources={r"/*": {"origins": "*"}})  # Enable CORS for all routes and origins

@app.route('/')
def Home():
    return 'Home'
@app.route('/rc4-encrypt' , methods=['POST'])
@app.route('/aes-encrypt', methods=['POST'])
def aes_encrypt_cipher():
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'Please provide both "text" and "key" in the request body.'}), 400

    input_text = data['text'].lower()
    
    encrypted_text = aes_encrypt(input_text)

    return jsonify({
        'original_text': input_text,
        'encrypted_text': encrypted_text
    })
    
@app.route('/aes-decrypt', methods=['POST'])
def aes_decrypt_cipher():
    data = request.get_json()
    
    if not data or 'text' not in data or 'tag' not in data:
        return jsonify({'error': 'Please provide both "text" and "key" in the request body.'}), 400

    encrypted_text = data['text'].lower()
    nonce = data['nonce']
    tag = data['tag']
    
    plain_text = aes_decrypt(nonce,encrypted_text,tag)

    return jsonify({
        'encrypted_text': encrypted_text,
        'plain_text': plain_text,
        'nonce':nonce,
        'tag':tag
    })
    
    
    
    
@app.route('/vignere-encrypt', methods=['POST'])
def vigenere_encrypt_cipher():
    data = request.get_json()
    
    if not data or 'text' not in data or 'key' not in data:
        return jsonify({'error': 'Please provide both "text" and "key" in the request body.'}), 400

    input_text = data['text'].lower()
    key = data['key']
    
    key_string = generate_key_string(input_text, key)
    encrypted_text = encrypt_data(input_text, key_string)

    return jsonify({
        'original_text': input_text,
        'key': key,
        'encrypted_text': encrypted_text
    })
    
@app.route('/vignere-decrypt', methods=['POST'])
def vigenere_decrypt_cipher():
    data = request.get_json()
    
    if not data or 'text' not in data or 'key' not in data:
        return jsonify({'error': 'Please provide both "text" and "key" in the request body.'}), 400

    encrypted_text = data['text'].lower()
    key = data['key']
    
    key_string = generate_key_string(encrypted_text, key)
    plain_text = decrypt_data(encrypted_text, key_string)

    return jsonify({
        'encrypted_text': encrypted_text,
        'key': key,
        'plain_text': plain_text
    })
    
@app.route('/playfair-encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    
    if not data or 'text' not in data or 'key' not in data:
        return jsonify({'error': 'Please provide both "text" and "key" in the request body.'}), 400

    plain_text = data['text'].lower()
    key = data['key']
    cipher_text = encrypt(plain_text, key)

    return jsonify({
        'encrypted_text': cipher_text,
        'key': key,
        'plain_text': plain_text
    })

@app.route('/playfair-decrypt', methods=['POST'])  # Fixed the route name
def playfair_decrypt():
    data = request.get_json()
    
    if not data or 'text' not in data or 'key' not in data:
        return jsonify({'error': 'Please provide both "text" and "key" in the request body.'}), 400

    cipher_text = data['text'].lower()
    key = data['key']
    plain_text = Decrypt(cipher_text, key)

    return jsonify({
        'decrypted_text': plain_text,
        'key': key,
        'cipher_text': cipher_text
    })

@app.route('/diffie-encrypt', methods=['POST'])
def diffie_encrypt():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'Please provide "text" in the request body.'}), 400

    plain_text = data['text']
    
    # Simulated Diffie-Hellman shared secret
    shared_secret = 123456  
    aes_key = hashlib.sha256(str(shared_secret).encode()).digest()  # Convert to 256-bit AES key

    cipher_text = diffie_encrypt_message(plain_text, aes_key)

    return jsonify({
        'encrypted_text': cipher_text,
        'plain_text': plain_text
    })


@app.route('/diffie-decrypt', methods=['POST'])  
def diffie_decrypt():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'Please provide "text" in the request body.'}), 400

    cipher_text = data['text']
    
    # Simulated Diffie-Hellman shared secret (must be same as used in encryption)
    shared_secret = 123456  
    aes_key = hashlib.sha256(str(shared_secret).encode()).digest()  # Convert to 256-bit AES key

    plain_text = diffie_decrypt_message(cipher_text, aes_key)

    return jsonify({
        'decrypted_text': plain_text,
        'cipher_text': cipher_text
    })

if __name__ == "__main__":
    app.run(debug=True)
