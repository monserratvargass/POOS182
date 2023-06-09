from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:

    def __init__(self):
        pass

    def conexionBD(self):
        try:
            conexion=sqlite3.connect("C:/Users/monse/Documents/POO/Diseño de interfaces P1/POOS182/Practica No.4/BDAlmacenDeBebidas.db")
            print("Conectado a la BD")
            return conexion #Devuelve el valor de la conexion
        except sqlite3.OperationalError:
             print("No se pudo conectar a la BD")

    def DarAlta(self,nom,precio,clas,marca):
        #1.Mandar llamar el metodo conexion
        conex=self.conexionBD()

        #2.Validar vacios
        if(nom==""or precio=="" or clas=="" or marca==""):
            messagebox.showwarning("Aguas!!!","Formulario incompleto")
            conex.close()
        else:
            #3.Realizar insert a BD
            #4. Preparamos las variables necesarias
            cursor=conex.cursor()
            #conH=self.encriptarContra(con)
            datos=(nom,precio,clas,marca)
            sqlInsert="insert into AlmacenBebidas(Nombre,Precio,Clasificacion,Marca) values(?,?,?,?)"

            #5.Ejecutamos el Insert
            cursor.execute(sqlInsert,datos)
            conex.commit()
            conex.close()
            messagebox.showinfo("Exito","Usuario guardado")
        
    def DarBaja(self,id):
         #1.Realizar conexion BD
        conx=self.conexionBD()
        #2.Verificar que el id vacio
        if(id==""):
            messagebox.showwarning("Cuidado","Escribe un identificador")
            conx.close()
        else:
            #3.Ejecutar lo de eliminar
            try:
                cursor=conx.cursor()
                sqlEliminar="delete from AlmacenBebidas where id="+id #Se eliminaran los registros a partir del id seleccionado
                #Ejecutamos y cerramos conexion
                cursor.execute(sqlEliminar)
                Elmusuario=cursor.fetchall() #Toma lo que esta en el cursor, mueve hacia la vista
                conx.commit()
                conx.close()

                return Elmusuario
            except sqlite3.OperationalError:
                print("No se puede ejecutar la funcion eliminar")
    
    def Actualizar(self,id,nom,precio,clas,marca):
         #1.Realizar conexion BD
        conx=self.conexionBD()
        #2.Verificar que el id vacio
        if(id==""):
            messagebox.showwarning("Cuidado","Escribe un identificador")
            conx.close()
        else:
            #3.Ejecutar la consulta
            try:
                cursor=conx.cursor()
                sqlUpdate="update AlmacenBebidas set Nombre=?, Precio=?, Clasificacion=?, Marca=? where id="+id #Se actualizaran los registros a partir del id seleccionado
                #Ejecutamos y cerramos conexion
                datos1=(nom,precio,clas,marca)
                cursor.execute(sqlUpdate,datos1)
                UPusuario=cursor.fetchall() #Toma lo que esta en el cursor, mueve hacia la vista
                conx.commit()
                conx.close()

                return UPusuario
            except sqlite3.OperationalError:
                print("Error de actualizacion")
    
    def Mostrar(self):
        #Conexion a la BD
        conx=self.conexionBD()
        try:
            cursor=conx.cursor()
            sqlConsulta="select * from AlmacenBebidas"

            cursor.execute(sqlConsulta)
            rsusuario=cursor.fetchall()
            conx.close()

            return rsusuario
        except sqlite3.OperationalError:
            print("Error de importar usuarios")

    def Calcular(self):
         #1.Realizar conexion BD
        conx=self.conexionBD()
        #2.Verificar que el id vacio
        #if(precio==""):
            #messagebox.showwarning("Cuidado","Escribe un identificador")
        #conx.close()
        #else:
            #3.Ejecutar la consulta
        try:
            cursor=conx.cursor()
            sqlCalculate="select avg(Precio) from AlmacenBebidas" #Promedio del precio de la tabla almacenBebidas
            #Ejecutamos y cerramos conexion
            #datos1=(precio)
            cursor.execute(sqlCalculate)
            Calusuario=cursor.fetchall() #Toma lo que esta en el cursor, mueve hacia la vista
            promedio=Calusuario [0]
            conx.commit()
            messagebox.showinfo('Promedio','El precio promedio de las bebidas es:'+str(promedio))
            conx.close()

            return Calusuario
        except sqlite3.OperationalError:
            print("Error de calculo")
            
    def ContarXMarca(self,marca):
         #1.Realizar conexion BD
        conx=self.conexionBD()
        #2.Verificar que el id vacio
        if(marca==""):
            messagebox.showwarning("Cuidado","Escribe una marca")
            conx.close()
        else:
            #3.Ejecutar la consulta
            try:
                cursor=conx.cursor()
                sqlContar1="select count(*) from AlmacenBebidas where Marca= ?" #buscar por marca
                #Ejecutamos y cerramos conexion
                datos1=(marca)
                cursor.execute(sqlContar1,(datos1,))
                UPusuario=cursor.fetchall() #Toma lo que esta en el cursor, mueve hacia la vista
                marcabebidas=UPusuario[0]
                conx.commit()
                messagebox.showinfo('Bebidas por marca','Cantidad por marca'+marca+'es:'+str(marcabebidas))
                conx.close()

                return UPusuario
            except sqlite3.OperationalError:
                print("Error de consulta")

    def ContarXClasificacion(self,clas):
         #1.Realizar conexion BD
        conx=self.conexionBD()
        #2.Verificar que el id vacio
        if(clas==""):
            messagebox.showwarning("Cuidado","Escribe una clasificacion")
            conx.close()
        else:
            #3.Ejecutar la consulta
            try:
                cursor=conx.cursor()
                sqlContar1="select count(*) from AlmacenBebidas where Clasificacion= ?" #Buscar por clasificacion
                #Ejecutamos y cerramos conexion
                datos1=(clas)
                cursor.execute(sqlContar1,(datos1,))
                UPusuario=cursor.fetchall() #Toma lo que esta en el cursor, mueve hacia la vista
                marcaclasificacion=UPusuario[0]
                conx.commit()
                messagebox.showinfo('Bebidas por marca','Cantidad por marca'+clas+'es:'+str(marcaclasificacion))
                conx.close()

                return UPusuario
            except sqlite3.OperationalError:
                print("Error de consulta")