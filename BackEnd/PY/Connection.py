from flask import Flask, request, jsonify
from sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection
host='localhost'
user='postgres'
password='Password1'
database='DB_Daan'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password1@localhost/DB_Daan' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

# Define the database model
class User(db.Model):
    Prid = db.Column(db.String(7), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    Password = db.Column(db.String(25), unique=True, nullable=False)
    role = db.Column(db.String(1), nullable=False)  # Assuming role is a single character

    def __repr__(self):
        return f'<User {self.username}>'

# Search for users
@app.route('/search', methods=['GET'])
def search_users():
    Prid = request.args.get('Prid')
    Password = request.args.get('Password')

    query = User.query

    if Prid:
        query = query.filter(User.Prid.like(f'%{Prid}%'))
    
    if Password:
        query = query.filter(User.Password.like(f'%{Password}%'))
    
    users = query.all()
    return jsonify([{'Prid': user.Prid, 'username': user.username, 'Password': user.Password, 'role': user.role} for user in users])
        
# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
