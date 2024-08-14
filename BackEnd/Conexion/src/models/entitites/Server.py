class Server():
    #Iniciacion de objeto user
    def __init__(self,id,name=None,password=None):
        self.id=id
        self.name=name
        self.password=password
    #Metodo de respuesta Json
    def to_JSON(self):
        return {
            'id':self.id,
            'name':self.name,
            'password':self.password,   
        }
