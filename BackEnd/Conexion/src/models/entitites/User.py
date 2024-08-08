class User():
    #Iniciacion de objeto user
    def __init__(self,id,display_name=None,prid=None,password=None,reset_password=None,type=None):
        self.id=id
        self.display_name=display_name
        self.prid=prid
        self.password=password
        self.reset_password=reset_password
        self.type=type
    #Metodo de respuesta Json
    def to_JSON(self):
        return {
            'id':self.id,
            'display_name':self.display_name,
            'prid':self.prid,
            'password':self.password,
            'reset_password':self.reset_password,     
            'type':self.type   
        }
