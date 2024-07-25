from flask import Blueprint , jsonify, request
import uuid

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
    
#Ruta para traer un usuario 
@main.route('/<prid>,<password>')
def get_user(prid,password):
    try:
        user=UserModel.search_Users(prid,password)
        if user != None:
            return jsonify(user)
        else:
            return "<h1>Usuario no encontrado</h1>",404
    except Exception as ex:
        return jsonify({'Message':str(ex)}),500
        
#Ruta para añadir un usuario
@main.route('/add',methods=['POST'])
def add_user():
    try:
        id=request.json['id']
        display_name=request.json['display_name']
        prid=request.json['prid']
        password=request.json['password']
        reset_password=request.json['reset_password']
        user=User(id,display_name,prid,password,reset_password)
        affected_rows=UserModel.add_Users(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return "<h1>Usuario no creado</h1>",500
    except Exception as ex:
        return jsonify({'Message':str(ex)}),500
    
#Ruta para borrar usuarios
@main.route('/delete/<id>',methods=['DELETE'])
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