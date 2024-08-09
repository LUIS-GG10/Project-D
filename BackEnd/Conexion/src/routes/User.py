from flask import Blueprint , jsonify, request
import uuid
from Encrypt.Encrypt import encrypt_data,decrypt_data

#Models
from models.UserModels import UserModel
from models.entitites.User import User

main=Blueprint('movie_blueprint',__name__)
#Ruta para traer todos los usarios
@main.route('/')
def get_users():
    try:
        users=UserModel.get_Users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'Message':str(ex)}),500
    
# Minimal route for user authentication
@main.route('/Validate', methods=['POST'])
def get_user():
    try:
        # Extract data from the request body
        data = request.get_json()
        prid = data.get('prid')
        password = data.get('password')

        if not prid or not password:
            return jsonify({'Message': 'Missing required parameters'}), 400

        encryptPass = encrypt_data(password)
        user = UserModel.search_Users(prid, encryptPass)
        
        if user:
            return  jsonify(user),200
        else:
            return jsonify({'Message': 'Usuario no encontrado'}), 404
    except Exception as ex:
        return jsonify({'Message': str(ex)}), 500
        
#Ruta para añadir un usuario
@main.route('/',methods=['POST'])
def add_user():
    try:
        id=request.json['id']
        display_name=request.json['display_name']
        prid=request.json['prid']
        password=request.json['password']
        passwordEncrypt=encrypt_data(password)
        reset_password=request.json['reset_password']
        user=User(id,display_name,prid,passwordEncrypt,reset_password)
        affected_rows=UserModel.add_Users(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return "<h1>Usuario no creado</h1>",500
    except Exception as ex:
        return jsonify({'Message':str(ex)}),500
    
#Ruta para borrar usuarios
@main.route('/<id>',methods=['DELETE'])
def delete_user(id):
    try:
        user=User(id)
        affected_rows=UserModel.dekete_Users(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return "<h1>NOOOO</h1>",404
    except Exception as ex:
        return jsonify({'Message':str(ex)}),500