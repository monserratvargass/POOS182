from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
#*Importar
from controlador import *
#1-Import tkinter module, ttk submodule and the showinfo from tkinter.messagebox
from tkinter.messagebox import showinfo

#*Crear instancia: puente entre los dos archivos
controlador= controladorBD()

#*Metodo que usa mi objeto controlador para insertar
def ejecutarAlta():
    controlador.DarAlta(varNom.get(),varPrecio.get(),varClas.get(),varMarca.get())

def ejecutarBaja():
    #Solicitar una confirmacion antes de Eliminar
        #DELUSU=controlador.eliminarUsuario(varElim.get())
    datose=tabla.get_children()

    for datoe in datose:
        tabla.delete(datoe)

        #for delete in DELUSU:
            #deletecadena=str(delete[0])+" "+delete[1]+" "+delete[2]+" "+str(delete[3])
    #pregunta
    ask=messagebox.askyesno('Pregunta','¿Estas seguro de eliminar el registro?')
    #Condiciones para verdadero el registro es eliminado de lo contrario no se elimina
    if ask==True:
        DELUSU=controlador.DarBaja(varElim.get())
        for delete in DELUSU:
            deletecadena=str(delete[0])+" "+delete[1]+" "+delete[2]+" "+str(delete[3])

            tabla.delete('',tk.END, values=deletecadena)

            tabla.bind('<<TreeviewSelect>>', ejecutarBaja)

        messagebox.showinfo('Confirmacion','Su registro seleccionado ha sido eliminado')

    else:
        messagebox.showerror('Error','Su registro seleccionado no ha sido eliminado')

def ejecutaModificar():
    #Avisar al usuario despues de modificar un registro.
    #controlador.actualizarUsuario(varNom1.get(),varCo1.get(),varPass1.get())
    datosm=tabla.get_children() #Para que se borren los datos ya consultados

    for datom in datosm:
        tabla.delete(datom)

    MODUSU=controlador.Actualizar(varAct.get(),varNom1.get(),varPrecio1.get(),varClas1.get(),varMarca1.get())
    #Ciclo for, cadena de actualizacion, mandar llamar las variables que serian los campos que se van actualizar con su respectiva posicion
    for modificar in MODUSU:
        updatecadena=str(modificar[0])+" "+modificar[1]+" "+modificar[2]+" "+str(modificar[3])+" "+str(modificar[4])

        tabla.update('',tk.END, values=updatecadena)

        varNom1.set(tabla.item('',"values")[1])
        varPrecio1.set(tabla.item('',"values")[2])
        varClas1.set(tabla.item(' ',"values")[3])
        varMarca1.set(tabla.item(' ',"values")[4])

        tabla.bind('<<TreeviewSelect>>', ejecutaModificar)

    messagebox.showinfo('Confirmacion','El registro se ha modificado')

#Metodo que usa mi objeto contrlador para consultar usuarios
def ejecutaMostrar():
      RSUSU=controlador.Mostrar()
      datosc=tabla.get_children() #Para que se borren los datos ya consultados

      for datoc in datosc:
          tabla.delete(datoc)
    
      for USU in RSUSU:
          cadenacon=str(USU[0])+" "+USU[1]+" "+str(USU[2])+" "+USU[3]+" "+USU[4]

          tabla.insert('',tk.END, values=cadenacon)

          #textCon.config(state='normal')
          #textCon.delete(2.0,'end')
          #textCon.insert('end',cadena+'\n')
          #textCon.config(state='disabled')

          tabla.bind('<<TreeviewSelect>>', ejecutaMostrar)

def ejecutaPromedio():
    controlador.Calcular()

def ejecutaContarMarca():
    controlador.ContarXMarca(varmar.get())

def ejecutaContarClasificacion():
    controlador.ContarXClasificacion(varclasif.get())

ventana=Tk()
ventana.title("Almacen de bebidas")
ventana.geometry("500x300")

panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)
pestana5=ttk.Frame(panel)
pestana6=ttk.Frame(panel)
pestana7=ttk.Frame(panel)

#Definir el contenido de cada una de las pestañas
#Pestaña 1: Dar de alta
titulo1=Label(pestana1,text="Dar de alta",fg="blue",font=("Modern",18)).pack()

varNom=tk.StringVar()
lblNom=Label(pestana1,text="Nombre: ").pack()
txtNom=Entry(pestana1,textvariable=varNom).pack()

varPrecio=tk.StringVar()
lblPrecio=Label(pestana1,text="Precio: ").pack()
txtPrecio=Entry(pestana1,textvariable=varPrecio).pack()

varClas=tk.StringVar()
lblClas=Label(pestana1,text="Clasificacion: ").pack()
txtClas=Entry(pestana1,textvariable=varClas).pack()

varMarca=tk.StringVar()
lblMarca=Label(pestana1,text="Marca: ").pack()
txtMarca=Entry(pestana1,textvariable=varMarca).pack()

#*Command
btnGuardar=Button(pestana1,text='Guardar registro',command=ejecutarAlta).pack()

#Pestaña 2: Dar de baja

titulo2=Label(pestana2,text="Dar de baja",fg="green",font=("Modern",18)).pack()

varElim=tk.StringVar()
lblElim=Label(pestana2,text="Identificador de registro:").pack()
txtElim=Entry(pestana2,textvariable=varElim).pack()

btnEliminar=Button(pestana2,text="Eliminar registro",command=ejecutarBaja).pack()

#Pestaña 3: Actualizar
titulo3=Label(pestana3,text="Actualizar registro",fg="green",font=("Modern",18)).pack()

varAct=tk.StringVar()
lblact=Label(pestana3,text="Identificador de registro:").pack()
txtact=Entry(pestana3,textvariable=varAct).pack()
#btnActualizar=Button(pestana4,text="Actualizar",command=ejecutaModificarU).pack()

#Ingreso nuevo para actualizar
varNom1=tk.StringVar()
lblNom1=Label(pestana3,text="Nombre: ").pack()
txtNom1=Entry(pestana3,textvariable=varNom1).pack()

varPrecio1=tk.StringVar()
lblPrecio1=Label(pestana3,text="Precio: ").pack()
txtPrecio1=Entry(pestana3,textvariable=varPrecio1).pack()

varClas1=tk.StringVar()
lblClas1=Label(pestana3,text="Clasificacion: ").pack()
txtClas1=Entry(pestana3,textvariable=varClas1).pack()

varMarca1=tk.StringVar()
lblMarca1=Label(pestana3,text="Marca: ").pack()
txtMarca1=Entry(pestana3,textvariable=varMarca1).pack()

btnActualizar=Button(pestana3,text="Actualizar",command=ejecutaModificar).pack()

#Pestaña 4: Consultar todos los usuarios

titulo4=Label(pestana4,text="Consulta de usuario:",fg="pink",font=("Modern",18)).pack()

btnConsulta=Button(pestana4,text="Buscar",command=ejecutaMostrar).pack()

subCon=Label(pestana4,text="Todos los registrados",fg="blue",font=("Modern",15)).pack()
textCon=tk.Text(pestana4,height=10,width=104)
textCon.pack()

#2-Define identifiers for columns
columnas=('ID','Nombre','Precio','Clasificacion','Marca')
#3-Create a Tkinter´s Treeview widget
tabla=ttk.Treeview(textCon,columns=columnas,show='headings')
#5-Specify the headings for the columns
tabla.heading('ID',text='ID')
tabla.heading('Nombre',text='NOMBRE')
tabla.heading('Precio',text='PRECIO')
tabla.heading('Clasificacion',text='CLASIFICACION')
tabla.heading('Marca',text='MARCA')

tabla.pack()

#Pestaña 5 calcular promedio

titulo5=Label(pestana4,text="Promedio precio:",fg="pink",font=("Modern",18)).pack()

'''subBus=Label(pestana5,text="Promedio de precios",fg="green",font=("Modern",18)).pack()
textBus=tk.Text(pestana4,height=10,width=104)
textBus.pack()'''

btnCalcularPromedio=Button(pestana5,text="Calcular",command=ejecutaPromedio).pack()

#pestaña 6 para contar las bebidas por marca

titulo6=Label(pestana6,text="Cantidad por marca",fg="green",font=("Modern",18)).pack()

varmar=tk.StringVar()
lblmar=Label(pestana6,text="Marca:").pack()
txtmar=Entry(pestana6,textvariable=varmar).pack()

btnContarMarca=Button(pestana6,text="Contar",command=ejecutaContarMarca).pack()

#pestaña 7 para contar las bebidas por clasificacion

titulo7=Label(pestana7,text="Cantidad por clasificaacion",fg="green",font=("Modern",18)).pack()

varclasif=tk.StringVar()
lblclasif=Label(pestana7,text="Clasificacion:").pack()
txtclasif=Entry(pestana7,textvariable=varclasif).pack()

btnContarClasificacion=Button(pestana7,text="Contar",command=ejecutaContarClasificacion).pack()


panel.add(pestana1, text="Dar de alta")
panel.add(pestana2, text="Dar de baja")
panel.add(pestana3, text="Actualizar ")
#Nueva pestaña para eliminar usuarios
panel.add(pestana4, text="Mostrar")
panel.add(pestana5, text="promedio")
panel.add(pestana6, text="Contar Marca")
panel.add(pestana7, text="Contar Clasificacion")

ventana.mainloop()