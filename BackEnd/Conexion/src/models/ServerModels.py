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
                cursor.execute('SELECT id, name, password, "hashPassword", "HostName", "OS", "IP", "PhysicalServer", "LogLocation", "Type" FROM public.servers')
                resultset = cursor.fetchall()

                for row in resultset:
                    server = Server(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    servers.append(server.to_JSON())
            connection.close()
            return servers
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod 
    def get_Server(cls, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT id, name, password,"hashPassword", "HostName", "OS", "IP", "PhysicalServer", "LogLocation", "Type" FROM servers WHERE id = %s',
                    (id,)
                )
                row = cursor.fetchone()
                server = None
                if row:
                    server = Server(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    server = server.to_JSON()
            connection.close()
            return server
        except Exception as ex:
            raise Exception(ex)

    # Método para obtener un usuario por prid y password
    @classmethod 
    def search_Server(cls, name):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT id, name, password,"hashPassword", "HostName", "OS", "IP", "PhysicalServer", "LogLocation", "Type" FROM servers WHERE name = %s',
                    (name)
                )
                row = cursor.fetchone()
                server = None
                if row:
                    server = Server(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
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
                    'INSERT INTO servers (id, name, password, "hashPassword", "HostName", "OS", "IP", "PhysicalServer", "LogLocation","Type") VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s,%s)',
                    (server.id, server.name, server.password, server.hashPassword, server.HostName,server.OS,server.IP,server.PhysicalServer,server.LogLocation,server.Type)

                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    # # Método para modificar usuarios 
    # @classmethod
    # def update_Servers(cls, server):
    #     try:
    #         connection = get_connection()
    #         with connection.cursor() as cursor: 
    #             cursor.execute("""UPDATE servers SET name = %s, password = %s, "hashPassword" = %s, "HostName"= %s , "OS" = %s, "IP" = %s, "PhysicalServer"= %s,"LogLocation"=%s, "Type"=%s WHERE id = %s""",
    #                            (server.id, server.name, server.password, server.hashPassword, server.HostName,server.OS,server.IP,server.PhysicalServer,server.LogLocation,server.Type))
    #             affected_rows=cursor.rowcount
    #             connection.commit()
                
    #         connection.close()
    #         return affected_rows
    #     except Exception as ex:
    #         raise Exception(ex)


    # Método para modificar usuarios 
    @classmethod
    def update_Servers(cls, server):
        try:
            connection = get_connection()
            with connection.cursor() as cursor: 
                cursor.execute("""UPDATE servers SET password = %s, "hashPassword" = %s WHERE id = %s""",
               (server.password, server.hashPassword, server.id))
                affected_rows=cursor.rowcount
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
