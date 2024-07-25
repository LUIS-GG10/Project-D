from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Generar una clave y un IV
key = os.urandom(32)  # AES-256 requiere una clave de 32 bytes
iv = os.urandom(16)   # El IV debe ser de 16 bytes

# Crear un cifrador AES en modo CBC
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

# Datos a cifrar
data = bytes(input("Ingresa la contraseña: "),'utf-8')

# Añadir padding al mensaje
padder = padding.PKCS7(algorithms.AES.block_size).padder()
padded_data = padder.update(data) + padder.finalize()

# Cifrar los datos
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

# Descifrar los datos
decryptor = cipher.decryptor()
decrypted_padded_data = decryptor.update(ciphertext) + decryptor.finalize()

# Quitar el padding
unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

print(f"Cifrado: {ciphertext}")
print(f"Descifrado: {decrypted_data.decode('utf-8')}")
