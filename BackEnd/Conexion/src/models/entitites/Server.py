class Server():
    #Iniciacion de objeto user
    def __init__(self,id,name=None,password=None,hashPassword=None,HostName=None,OS=None,IP=None,PhysicalServer=None,LogLocation=None,Type=None):
        self.id=id
        self.name=name
        self.password=password
        self.hashPassword=hashPassword
        self.HostName=HostName
        self.OS=OS
        self.IP=IP
        self.PhysicalServer=PhysicalServer
        self.LogLocation=LogLocation
        self.Type=Type
    #Metodo de respuesta Json
    def to_JSON(self):
        return {
            'id':self.id,
            'name':self.name,
            'password':self.password,   
            'hashPassword':self.hashPassword,
            'HostName':self.HostName,
            "OS":self.OS,
            "IP":self.IP,
            "PhysicalServer":self.PhysicalServer,
            "LogLocation":self.LogLocation,
            "Type":self.Type
        }
