from flask import Flask, request, jsonify
from vigenere_cipher import generate_key_string, encrypt_data , decrypt_data
from playfair import encrypt,Decrypt
app = Flask(__name__)


@app.route('/')
def Home():
    return 'Home'

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
    
    
@app.route('/vignere-decrypt' , methods=['POST'])
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
    
@app.route('/playfair-encrypt' , methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    
    if not data or 'text' not in data or 'key' not in data:
        return jsonify({'error': 'Please provide both "text" and "key" in the request body.'}), 400

    plain_text = data['text'].lower()
    key = data['key']
    
    cipher_text = encrypt(plain_text , key )
    

    return jsonify({
        'encrypted_text': cipher_text,
        'key': key,
        'plain_text': plain_text
    })

@app.route('/playfair-encrypt' , methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    
    if not data or 'text' not in data or 'key' not in data:
        return jsonify({'error': 'Please provide both "text" and "key" in the request body.'}), 400

    cipher_text = data['text'].lower()
    key = data['key']
    
    plain_text = Decrypt(cipher_text , key )
    

    return jsonify({
        'decrypted_text': plain_text,
        'key': key,
        'cipher_text': cipher_text
    })
    
if __name__ == "__main__":
    app.run(debug=True)
