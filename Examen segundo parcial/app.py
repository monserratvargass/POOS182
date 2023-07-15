#nombre.server.py o app.py
from flask import Flask, render_template, request, redirect,url_for,flash #Importar libreria
from flask_mysqldb import MySQL

app=Flask(__name__) #Inicializacion del servidor Flask

#Configuraciones para la conexion de   
app.config['MYSQL_HOST']="localhost" #Especificar en que servidor trabajamos
app.config['MYSQL_USER']="root" #Especificar usuario
app.config['MYSQL_PASSWORD']="" #Especificar contraseña
app.config['MYSQL_DB']="dbfloreria" #Especificar a que base de datos

app.secret_key='mysecretkey' #Permite hacer envios a traves de post

mysql=MySQL(app)

@app.route('/')
def index():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from tbflores')
    consulta=curSelect.fetchall()
    
    return render_template('index.html', Cfloreria=consulta)

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method=='POST':
        Nnombre=request.form['nombre']
        Ncantidad=request.form['cantidad']
        Nprecio=request.form['precio']

        CS=mysql.connection.cursor()
        CS.execute('insert into tbflores(nombre,cantidad,precio) values(%s,%s,%s)',(Nnombre,Ncantidad,Nprecio))
        mysql.connection.commit()
    flash('Registro agregado')
    return redirect(url_for('index'))

@app.route('/eliminar/<id>',methods=['POST'])
def eliminar(id):
    if request.method=='POST':
        Nnombre=request.form['nombre']
        Ncantidad=request.form['cantidad']
        Nprecio=request.form['precio']

        CS=mysql.connection.cursor()
        CS.execute('delete from tbflores where id=%s',(id))
        mysql.connection.commit()
    flash('Registro eliminado')
    return redirect(url_for('index'))

@app.route('/borrar/<id>')
def borrar(id):
    curBorrar=mysql.connection.cursor()
    curBorrar.execute('select * from tbflores where id= %s', (id,))#Coma importante por que lo confunde con una tupla
    consultaID=curBorrar.fetchone() #Para traer unicamente un registro

    return render_template('eliminarFloreria.html', floreria=consultaID)

if __name__=='__main__':
    app.run(port=5000,debug=True)