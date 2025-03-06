from flask import Flask, request, jsonify
from cipher.vigenere import VigenereCipher


app = Flask(__name__)
# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plaintext = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plaintext, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']

    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)

    return jsonify({'decrypted_text': decrypted_text})

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)