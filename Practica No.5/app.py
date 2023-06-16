#nombre.server.py o app.py
from flask import Flask #Importar libreria

app=Flask(__name__) #Inicializacion del servidor Flask

#Configuraciones para la conexion de BD
app.config['MYSQL_HOST']="localhost" #Especificar en que servidor trabajamos
app.config['MYSQL_USER']="root" #Especificar usuario
app.config['MYSQL_PASSWORD']="" #Especificar contraseña
app.config['MYSQL_DB']="dbflask" #Especificar a que base de datos

#Declaracion de rutas

#Declarar ruta Index/principal http//localhost:5000
#Ruta se compone de nombre y funcion
@app.route('/')
def index():
    return "Hola mundo"

@app.route('/guardar')
def guardar():
    return "Se guardo el album en la BD"

@app.route('/eliminar')
def eliminar():
    return "Se elimino el almbun de la BD"

#Ejecucion del servidor
if __name__=='__main__':
    app.run(port=5000,debug=True) #Procurar que sea un puerto desocupado, debug(prendido)