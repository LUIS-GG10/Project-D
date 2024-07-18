import pandas as pd

def valida_info(busq):
    if(busq):
        print("Bienvenido")
    else:
        print("Contraseña o prid incorrecto") 

def busqueda(df,prind,password):
    busq = False
    for index, row in df.iterrows():
        if(row['Prid']== prind and row['Password']== password):
            busq = True
    return busq

prind = input("Prid: ")
password = input("Contraseña: ")

# Leer el archivo JSON
file_path = "Prueba.json"
df = pd.read_json(file_path)
valida_info(busqueda(df,prind,password))

print(df)