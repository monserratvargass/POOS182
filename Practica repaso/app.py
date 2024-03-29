#nombre.server.py o app.py
from flask import Flask, render_template, request, redirect,url_for,flash #Importar libreria
from flask_mysqldb import MySQL

app=Flask(__name__) #Inicializacion del servidor Flask

#Configuraciones para la conexion de   
app.config['MYSQL_HOST']="localhost" #Especificar en que servidor trabajamos
app.config['MYSQL_USER']="root" #Especificar usuario
app.config['MYSQL_PASSWORD']="" #Especificar contraseña
app.config['MYSQL_DB']="db_fruteria" #Especificar a que base de datos

app.secret_key='mysecretkey' #Permite hacer envios a traves de post


mysql=MySQL(app)

#Declaracion de rutas

#Declarar ruta Index/principal http//localhost:5000
#Ruta se compone de nombre y funcion
@app.route('/')
def index():
    '''curSelect=mysql.connection.cursor()
    curSelect.execute('select * from tbfrutas')
    consulta=curSelect.fetchall() #Para traer varios registros
    #print(consulta)'''
    return render_template('index.html') #Nos sirve para concatenar las consultas y abrir rutas

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        VFruta=request.form['txtFruta']
        VTemp=request.form['txtTemporada']
        Vprecio=request.form['txtPrecio']
        Vstock=request.form['txtStock']
        #print(titulo,artista,anio)
        CS=mysql.connection.cursor()
        CS.execute('insert into tbfrutas(fruta,temporada,precio,stock) values(%s,%s,%s,%s)',(VFruta,VTemp,Vprecio,Vstock)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Registro agregado correctamente')
    return redirect(url_for('index')) #Reedireccionamiento a la vista index

@app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        VFruta=request.form['txtFruta']
        VTemp=request.form['txtTemporada']
        Vprecio=request.form['txtPrecio']
        Vstock=request.form['txtStock']
    
        curUpdate=mysql.connection.cursor()
        curUpdate.execute('update tbfrutas set fruta=%s, temporada=%s, precio=%s, stock=%s where id=%s', (VFruta,VTemp,Vprecio,Vstock,id))
        mysql.connection.commit() #Para actualizar

    flash('Registro actualizado correctamente')
    return redirect(url_for('index')) #Reedireccionamiento a la vista index

@app.route('/editar/<id>')
def editar(id):
    curEditar=mysql.connection.cursor()
    curEditar.execute('select * from tbfrutas where id= %s', (id,))#Coma importante por que lo confunde con una tupla
    consultaID=curEditar.fetchone() #Para traer unicamente un registro

    return render_template('editarFruteria.html', fruteria=consultaID)

@app.route('/eliminar/<id>',methods=['POST'])
def eliminar(id):
    curDelete=mysql.connection.cursor()
    curDelete.execute('delete from tbfrutas where id=%s', (id)) 
    mysql.connection.commit() #Para actualizar

    flash('Registro eliminado correctamente')
    return redirect(url_for('index')) #Reedireccionamiento a la vista index

@app.route('/borrar/<id>')
def borrar(id):
    curBorrar=mysql.connection.cursor()
    curBorrar.execute('select * from tbfrutas where id= %s', (id,))#Coma importante por que lo confunde con una tupla
    consultaID=curBorrar.fetchone() #Para traer unicamente un registro

    return render_template('eliminarFruteria.html', fruteria=consultaID)

@app.route('/consultar')
def consultar():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from tbfrutas')
    consulta=curSelect.fetchall() #Para traer varios registros
    #print(consulta)
    return render_template('consultarFruteria.html', listaFruteria=consulta) #Nos sirve para concatenar las consultas y abrir rutas


@app.route('/buscar',methods=['POST'] )
def buscar():
    Varbuscar= request.form['txtbuscar']
    print(Varbuscar)
    CC= mysql.connection.cursor()
    CC.execute('select * from tbfrutas where fruta LIKE %s', (f'%{Varbuscar}%',))
    confruta= CC.fetchall()
    print(confruta)
    return render_template('buscarFruteria.html', listafruta = confruta)

#Ejecucion del servidor
if __name__=='__main__':
    app.run(port=5001,debug=True) #Procurar que sea un puerto desocupado, debug(prendido)