from database.db import get_connection
from models.entitites.User import User

class UserModel:
    # Método para traer todos los usuarios
    @classmethod
    def get_Users(cls):
        try:
            connection = get_connection()
            users = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, display_name, prid, password, reset_password FROM users")
                resultset = cursor.fetchall()

                for row in resultset:
                    user = User(row[0], row[1], row[2], row[3], row[4])
                    users.append(user.to_JSON())
            
            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    # Método para obtener un usuario por prid y password
    @classmethod 
    def search_Users(cls, prid, password):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT display_name, prid FROM users WHERE prid = %s AND password = %s",
                    (prid, password)
                )
                row = cursor.fetchone()
                user = None
                if row:
                    user = User(row[0], row[1])
                    user = user.to_JSON()
            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)

    # Método para añadir usuarios 
    @classmethod
    def add_Users(cls, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO users (id, display_name, prid, password, reset_password) VALUES (%s, %s, %s, %s, %s)",
                    (user.id, user.display_name, user.prid, user.password, user.reset_password)
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    # Método para borrar usuarios 
    @classmethod
    def delete_Users(cls, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE id = %s", (user.id,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
