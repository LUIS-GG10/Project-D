from database.db import get_connection
from models.entitites.Server import Server 

class ServerModel:
    # Método para traer todos los usuarios
    @classmethod
    def get_Servers(cls):
        try:
            connection = get_connection()
            servers = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, password,hashPassword FROM servers")
                resultset = cursor.fetchall()

                for row in resultset:
                    server = Server(row[0], row[1], row[2], row[3])
                    servers.append(server.to_JSON())
            
            connection.close()
            return servers
        except Exception as ex:
            raise Exception(ex)

    # Método para obtener un usuario por prid y password
    @classmethod 
    def search_Servers(cls, name):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, name, password,hashPassword FROM servers WHERE name = %s",
                    (name,)
                )
                row = cursor.fetchone()
                server = None
                if row:
                    server = Server(row[0], row[1], row[2], row[3])
                    server = server.to_JSON()
            connection.close()
            return server
        except Exception as ex:
            raise Exception(ex)

    # Método para añadir usuarios 
    @classmethod
    def add_Servers(cls, server):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO servers (id, name, password, hashPassword) VALUES (%s, %s, %s, %s)",
                    (server.id, server.name, server.password, server.hashPassword)

                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    # Método para borrar usuarios 
    @classmethod
    def delete_Servers(cls, server):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM servers WHERE id = %s", (server.id,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
