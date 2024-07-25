from database.db import get_connection
from .entitites.User import User

class UserModel():

    #Metodo para traer todos los usuarios
    @classmethod
    def get_Users(self):
        try:
            connection=get_connection()
            users=[]
            with connection.cursor()as cursor:
                cursor.execute("SELECT id,display_name,prid,password,reset_password FROM users")
                resultset=cursor.fetchall()

                for row in resultset:
                    user=User(row[0],row[1],row[2],row[3],row[4])
                    users.append(user.to_JSON())
            
            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)
    #Metodo para obtener un usuario por prid y passoword
    @classmethod 
    def search_Users(self,prid,password):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, display_name, prid, password, reset_password FROM users WHERE prid = %s AND password = %s",(prid,password,))
                row = cursor.fetchone()
                user = None
                if row:
                    user = User(row[0], row[1], row[2], row[3], row[4])
                    user= user.to_JSON()             
                connection.close()
                return user
        except Exception as ex:
            raise Exception(ex)
    
    #Metodo Para añadir usarios 
    @classmethod
    def add_Users(self,user):
        try:
            connection=get_connection()
            with connection.cursor()as cursor:
                cursor.execute("INSERT INTO users (id,display_name,prid,password,reset_password) VALUES(%s,%s,%s,%s,%s)",(user.id,user.display_name,user.prid,user.password,user.reset_password))
                affected_rows=cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    #Metodo para borrar usuarios 
    @classmethod
    def dekete_Users(self,user):
        try:
            connection=get_connection()
            with connection.cursor()as cursor:
                cursor.execute("DELETE from users where id=%s",(user.id,))
                affected_rows=cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

