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
        servers=ServerModel.get_Servers()
        return jsonify(servers)
    except Exception as ex:
        return jsonify({'Message':str(ex)}),500
    
@main.route('/search', methods=['POST'])
def get_server():
    try:
        # Extract data from the request body
        data = request.get_json()
        name = data.get('name')
 
        if not name :
            return jsonify({'Message': 'Missing required parameters'}), 400
        # Search for the server
        server = ServerModel.search_Server(name)
 
        if server:
            return jsonify(server), 200
        else:
            return jsonify({'Message': 'Server not found'}), 404
    except Exception as ex:
        return jsonify({'Message': str(ex)}), 500
    
    
    
#Ruta para añadir un usuario
@main.route('/',methods=['POST'])
def add_server():
    try:
        id=request.json['id']
        name=request.json['name']
        password=request.json['password']
        hashPassword=encrypt_data(password)
        IP=request.json['IP']
        HostName=request.json['HostName']
        LogLocation=request.json['LogLocation']
        OS=request.json['OS']
        PhysicalServer=request.json['PhysicalServer']
        type=request.json['type']
        
        
        server=Server(id,name,password,hashPassword,IP,HostName,LogLocation,OS,PhysicalServer,type)
        affected_rows=ServerModel.add_Servers(server)

        if affected_rows == 1:
            return jsonify(server.id)
        else:
            return "<h1>Server no creado</h1>",500
    except Exception as ex:
        return jsonify({'Message':str(ex)}),500
    

@main.route('/<id>', methods=['PUT'])
def update_server(id):
    try:
        password=request.json['password']
        hashPassword=encrypt_data(password)
        server=Server(id,None,password,hashPassword)
        affected_rows=ServerModel.update_Servers(server)

        if affected_rows == 1:
            return jsonify(server.id)
        else:
            return jsonify({'message':"Error on insert "}),500
    except Exception as ex:
        return jsonify({'Message': str(ex)}), 500

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