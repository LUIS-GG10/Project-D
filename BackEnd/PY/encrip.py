import bcrypt
# Ingresa la contraseña original
original_password = input("Ingresa tu contraseña: ")

# Convierte la contraseña a bytes
password_bytes = original_password.encode('utf-8')

# Genera una sal única
salt = bcrypt.gensalt()

# Encripta la contraseña con la sal generada
hashed_password = bcrypt.hashpw(password_bytes, salt)

# Guarda la contraseña encriptada en una base de datos o archivo
print("Contraseña encriptada:", hashed_password.decode('utf-8'))

original_password2 = input("Ingresa tu contraseña: ")
# Convierte la contraseña a bytes
password_bytes2 = original_password2.encode('utf-8')

if bcrypt.checkpw(password_bytes2, hashed_password):
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
