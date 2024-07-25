from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import base64

# Generar una clave y un IV
def generate_key():
    key = bytes.fromhex('f35367315a665c79d117982c158fb7035c19cde36ff247551f932165acacf206')
    iv = bytes.fromhex('7e74a84bd342f02447f2bd81462e4b21')
    return key, iv

# Cifrar los datos
def encrypt_data(password):
    key, iv = generate_key()
    data = bytes(password, 'utf-8')
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(ciphertext).decode('utf-8')  # Convertir a base64 para una representación segura en texto

# Descifrar los datos
def decrypt_data(ciphertext_base64):
    key, iv = generate_key()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    ciphertext = base64.b64decode(ciphertext_base64)
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    return decrypted_data.decode('utf-8')


# Obtener el texto a cifrar del usuario
password = input("Introduce la contraseña a cifrar: ")

# Cifrar la contraseña
encrypted_password = encrypt_data(password)
print(f"Cifrado: {encrypted_password}")

# Obtener el texto cifrado para descifrar
encrypted_input = input("Introduce el texto cifrado para descifrar: ")

# Descifrar el texto cifrado
decrypted_password = decrypt_data(encrypted_input)
print(f"Descifrado: {decrypted_password}")
