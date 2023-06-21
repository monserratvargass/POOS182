#nombre.server.py o app.py
from flask import Flask, render_template, request, redirect,url_for,flash #Importar libreria
from flask_mysqldb import MySQL

app=Flask(__name__) #Inicializacion del servidor Flask

#Configuraciones para la conexion de BD
app.config['MYSQL_HOST']="localhost" #Especificar en que servidor trabajamos
app.config['MYSQL_USER']="root" #Especificar usuario
app.config['MYSQL_PASSWORD']="" #Especificar contraseña
app.config['MYSQL_DB']="dbflask" #Especificar a que base de datos

app.secret_key='mysecretkey' #Permite hacer envios a traves de post

mysql=MySQL(app)

#Declaracion de rutas

#Declarar ruta Index/principal http//localhost:5000
#Ruta se compone de nombre y funcion
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vanio=request.form['txtAnio']
        #print(titulo,artista,anio)
        CS=mysql.connection.cursor()
        CS.execute('insert into album(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Album agregado correctamente')
    return redirect(url_for('index')) #Reedireccionamiento a la vista index

@app.route('/eliminar')
def eliminar():
    return "Se elimino el almbun de la BD"

#Ejecucion del servidor
if __name__=='__main__':
    app.run(port=5000,debug=True) #Procurar que sea un puerto desocupado, debug(prendido)