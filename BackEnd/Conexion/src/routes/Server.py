from flask import Blueprint , jsonify, request
import uuid
from Encrypt.Encrypt import encrypt_data,decrypt_data

#Models
from models.ServerModels import ServerModel 
from models.entitites.Server import Server

main=Blueprint('server_main',__name__)
#Ruta para traer todos los usarios
@main.route('/')
def get_servers():
    try:
        servers=ServerModel.get_Servers
        return jsonify(servers)
    except Exception as ex:
        return jsonify({'Message':str(ex)}),500
    
# # Minimal route for user authentication
# @main.route('/search', methods=['POST'])
# def get_servers():
#     try:
#         # Extract data from the request body
#         data = request.get_json()
#         prid = data.get('prid')
#         password = data.get('password')

#         if not prid or not password:
#             return jsonify({'Message': 'Missing required parameters'}), 400

#         encryptPass = encrypt_data(password)
#         user = UserModel.search_Users(prid, encryptPass)
        
#         if user:
#             # Ensure the 'type' is included in the user object
#             user_type = user.get('type')
#             if not user_type:
#                 return jsonify({'Message': 'User type not found'}), 500

#             if user_type == 'A':
#                 # Provide admin access
#                 return jsonify(user), 200
#             elif user_type == 'S':
#                 # Provide superuser access
#                 return jsonify(user), 200
#             elif user_type == 'U':
#                 # Provide standard user access
#                 return (user), 200
#             else:
#                 return jsonify({'Message': 'Unknown role'}), 403
#         else:
#             return jsonify({'Message': 'Usuario no encontrado'}), 404
#     except Exception as ex:
#         return jsonify({'Message': str(ex)}), 500
#Ruta para añadir un usuario
@main.route('/',methods=['POST'])
def add_server():
    try:
        id=request.json['id']
        name=request.json['name']
        password=request.json['password']
        server=Server(id,name,password)
        affected_rows=ServerModel.add_Servers(server)

        if affected_rows == 1:
            return jsonify(server.id)
        else:
            return "<h1>Usuario no creado</h1>",500
    except Exception as ex:
        return jsonify({'Message':str(ex)}),500
    
#Ruta para borrar usuarios
@main.route('/<id>',methods=['DELETE'])
def delete_user(id):
    try:
        server=Server(id)
        affected_rows=ServerModel.delete_Servers(server)

        if affected_rows == 1:
            return jsonify(server.id)
        else:
            return "<h1>NOOOO</h1>",404
    except Exception as ex:
        return jsonify({'Message':str(ex)}),500