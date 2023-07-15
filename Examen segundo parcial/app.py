from flask import Flask, render_template, request, redirect,url_for, flash
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MySQL_HOST']="localhost"
app.config['MySQL_USER']="root"
app.config['MySQL_PASSWORD']=""
app.config['MySQL_DB']="dbfloreria"

app.secret_key='mysecretkey'

mysql=MySQL(app)

@app.route('/')
def index():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from Floreria')
    consulta=curSelect.fetchall()
    
    return render_template('index.html', Cfloreria=consulta)

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method=='POST':
        Nnombre=request.form['nombre']
        Ncantidad=request.form['cantidad']
        Nprecio=request.form['precio']

        CS=mysql.connection.cursor()
        CS.execute('insert into floreria(nombre,cantidad,precio) values(%s,%s,%s)',(Nnombre,Ncantidad,Nprecio))
        mysql.connection.commit()
    flash('Registro agregado')
    return redirect(url_for('index'))

@app.route('/eliminar/<id>')
def eliminar(id):
    if request.method=='POST':
        Nnombre=request.form['nombre']
        Ncantidad=request.form['cantidad']
        Nprecio=request.form['precio']

        CS=mysql.connection.cursor()
        CS.execute('delete from floreria where id=%s',(id))
        mysql.connection.commit()
    flash('Registro eliminado')
    return redirect(url_for('index'))

@app.route('/borrar/<id>')
def borrar(id):
    curBorrar=mysql.connection.cursor()
    curBorrar.execute('select * from floreria where id= %s', (id,))#Coma importante por que lo confunde con una tupla
    consultaID=curBorrar.fetchone() #Para traer unicamente un registro

    return render_template('eliminarFloreria.html', floreria=consultaID)

if __name__=='__main__':
    app.run(port=5000,debug=True)