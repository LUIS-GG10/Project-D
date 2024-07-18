from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurar la conexión a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la extensión de SQLAlchemy
db = SQLAlchemy(app)

# Definir el modelo de la base de datos
class User(db.Model):
    Prid = db.Column(db.String(7), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    Password = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


# Buscar si existe
@app.route('/search', methods=['GET'])
def search_users(Prid, Password):
    query = User.query
    
    if Prid:
        query = query.filter(User.Prid(f'%{Prid}%'))
    
    if Password:
        query = query.filter(User.Password(f'%{Password}%'))
    
    users = query.all()
    return jsonify([{'Prid': user.Prid, 'username': user.username, 'Password': user.Password} for user in users])
        

#Iniciar 
if __name__ == '__main__':
    app.run(debug=True)