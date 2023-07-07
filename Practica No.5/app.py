#nombre.server.py o app.py
from flask import Flask, render_template, request, redirect,url_for,flash #Importar libreria
from flask_mysqldb import MySQL

app=Flask(__name__) #Inicializacion del servidor Flask

#Configuraciones para la conexion de   
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
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from album')
    consulta=curSelect.fetchall() #Para traer varios registros
    #print(consulta)
    return render_template('index.html', listaAlbum=consulta) #Nos sirve para concatenar las consultas y abrir rutas

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

@app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vanio=request.form['txtAnio']
    
        curUpdate=mysql.connection.cursor()
        curUpdate.execute('update album set titulo=%s, artista=%s, anio=%s where id=%s', (Vtitulo,Vartista,Vanio,id))
        mysql.connection.commit() #Para actualizar

    flash('Album actualizado correctamente')
    return redirect(url_for('index')) #Reedireccionamiento a la vista index

@app.route('/editar/<id>')
def editar(id):
    curEditar=mysql.connection.cursor()
    curEditar.execute('select * from album where id= %s', (id,))#Coma importante por que lo confunde con una tupla
    consultaID=curEditar.fetchone() #Para traer unicamente un registro

    return render_template('editarAlbum.html', album=consultaID)

@app.route('/eliminar/<id>',methods=['POST'])
def eliminar(id):
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vanio=request.form['txtAnio']
    
        curDelete=mysql.connection.cursor()
        curDelete.execute('delete from album where id=%s', (id)) 
        mysql.connection.commit() #Para actualizar

    flash('Album eliminado correctamente')
    return redirect(url_for('index')) #Reedireccionamiento a la vista index

@app.route('/borrar/<id>')
def borrar(id):
    curBorrar=mysql.connection.cursor()
    curBorrar.execute('select * from album where id= %s', (id,))#Coma importante por que lo confunde con una tupla
    consultaID=curBorrar.fetchone() #Para traer unicamente un registro

    return render_template('eliminarAlbum.html', album=consultaID)

#Ejecucion del servidor
if __name__=='__main__':
    app.run(port=5000,debug=True) #Procurar que sea un puerto desocupado, debug(prendido)