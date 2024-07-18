from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Ruta del archivo JSON
json_file_path = "Prueba.json"

# Función para cargar el JSON
def load_json():
    with open(json_file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Ruta para buscar usuarios por nombre de usuario y/o correo electrónico
@app.route('/search', methods=['GET'])
def search_users():
    data = load_json()
    prind = "Kxcr234"
    password = "Hersdsw124%"
    
    results = data
    
    if prind:
        results = [user for user in results if prind.lower() in user['Prid'].lower()]
    
    if password:
        results = [user for user in results if password.lower() in user['Password'].lower()]
    
    if results:
        return "Bienvenido"
    else:
        return "No valido"
    return jsonify(results)

# Ruta para mostrar todos los usuarios
@app.route('/users', methods=['GET'])
def get_users():
    data = load_json()
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)
