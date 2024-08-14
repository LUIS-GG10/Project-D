from flask import Flask 
from config import config
from flask_cors import CORS

#Importar Rutas 
from routes import User
from routes import Server
app=Flask(__name__)
CORS(app) 

def Page_not_Found(error):
    return"<h1> Pagina No disponible </h1>",404

if __name__== '__main__':
    app.config.from_object(config['development'])
    #BluePrint

    Server
    app.register_blueprint(User.main,url_prefix='/api/Users', name='user_main')
    app.register_blueprint(Server.main, url_prefix='/Principal')

    #Si no existe la pagina
    app.register_error_handler(404,Page_not_Found)
    app.run()
