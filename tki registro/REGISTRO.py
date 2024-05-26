import tkinter  ##santiago jimenez ferrer
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk




ventana_registro= tkinter.Tk()
ventana_registro.geometry("600x600")
ventana_registro.title("SISTEMA DE REGISTRO")
ventana_registro.configure(background="white")

path = Image.open("\\Users\\USUARIO\\Desktop\\tki registro\\tecnar.png")
icono = ImageTk.PhotoImage(path)
ventana_registro.iconphoto(True, icono)

image = Image.open("\\Users\\USUARIO\\Desktop\\tki registro\\fondo.jpg")
image = image.resize((200,130))
image = ImageTk.PhotoImage(image)
inicio_imagen = tkinter.Label(image=image,bg="white")
inicio_imagen.grid(row=1, column=0, padx=(0,0), pady=(0,0))

 
# Create the label objects and pack them using grid
Nombre = tkinter.Label(ventana_registro, text="NOMBRE: ")
Nombre.grid(row=1, column=0, padx=(50,0), pady=(160,0))

Apellido = tkinter.Label(ventana_registro, text="APELLIDO")
Apellido.grid(row=2, column=0, padx=(50,0), pady=(20,0))

Edad = tkinter.Label(ventana_registro, text="EDAD")
Edad.grid(row=3, column=0, padx=(50,0), pady=(20,0))

Direccion = tkinter.Label(ventana_registro, text="DIRECCION: ")
Direccion.grid(row=4, column=0, padx=(50,0), pady=(20,0))

Sexo = tkinter.Label(ventana_registro, text="SEXO")
Sexo.grid(row=5, column=0, padx=(50,0), pady=(20,0))

Ciudad = tkinter.Label(ventana_registro, text="CIUDAD")
Ciudad.grid(row=6, column=0, padx=(50,0), pady=(20,0))

telefono = tkinter.Label(ventana_registro, text="TELEFONO")
telefono.grid(row=7, column=0, padx=(50,0), pady=(20,0))

Confirmacion = tkinter.Label(ventana_registro, text="", bd= 0,background="white")
Confirmacion.grid(row=8, column=0, padx=(50,0), pady=(20,0))






e1 = tkinter.Entry(ventana_registro)
e2 = tkinter.Entry(ventana_registro)
e3 = tkinter.Entry(ventana_registro)
e4 = tkinter.Entry(ventana_registro)
e5 = tkinter.Entry(ventana_registro)


def selec():
    if opcion.get() == 1:
       Confirmacion.config(text="masculino",fg="white")
    if opcion.get() == 2:
       Confirmacion.config(text="femenino",fg="white")


    

opcion = IntVar() 

casilla_masculino = Radiobutton(ventana_registro, text="MASCULINO", variable=opcion, value=1, command=selec)
casilla_femenino = Radiobutton(ventana_registro, text="FEMENINO", variable=opcion,value=2, command=selec)


cuadro_lista = tkinter.Listbox(ventana_registro,width=20, height=5, selectmode="multiple")


def obtener_seleccion():

    global elemento
    seleccionados = cuadro_lista.curselection()
    for index in seleccionados:
        elemento = cuadro_lista.get(index)
        

elementos = ["Cartagena", "Barranquilla", "Bogota", "Medellin"]

for elemento in elementos:
    cuadro_lista.insert(tkinter.END, elemento)
    elemento = ""


    


def imprimir():
    
    entrada_nombre = e1.get()
    entrada_apellido = e2.get()
    entrada_edad = e3.get()
    entrada_direccion = e4.get()
    genero = Confirmacion["text"]
    obtener_seleccion()
    seleccion = elemento
    entrada_numero = e5.get()
    
    

    messagebox.showinfo("REGISTRO EXITOSO","Nombre: "+ entrada_nombre + "\n" + "Apellido: " + entrada_apellido + "\n" + "Edad: " + entrada_edad + "\n" + "Direccion: " + entrada_direccion + "\n" + "Sexo: " + genero + "\n" + "Ciudad:  " + seleccion  + "\n" + "Telefono:  " + entrada_numero )

button = tkinter.Button(text="REGISTRARSE", command=imprimir)



e1.grid(row=1, column=1, padx=(50,0), pady=(160,0))
e2.grid(row=2, column=1, padx=(50,0), pady=(20,0))
e3.grid(row=3, column=1, padx=(50,0), pady=(20,0))
e4.grid(row=4, column=1, padx=(50,0), pady=(20,0))
casilla_masculino.grid(row=5, column=1, padx=(50,0), pady=(20,0))
casilla_femenino.grid(row=5, column=2, padx=(50,0), pady=(20,0))
e5.grid(row=7, column=1, padx=(50,0), pady=(20,0))



cuadro_lista.grid(row=6, column=1, padx=(50,0), pady=(20,0))

button.grid(row=8, column=1, padx=(40,0), pady=(30,0))

 

ventana_registro.mainloop()