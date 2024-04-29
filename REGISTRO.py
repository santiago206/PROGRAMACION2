import tkinter  ##santiago jimenez ferrer
from tkinter import messagebox, ttk
from PIL import Image, ImageTk


ventana_registro= tkinter.Tk()
ventana_registro.geometry("600x520")
ventana_registro.title("SISTEMA DE REGISTRO")
ventana_registro.configure(background="white")

path = Image.open("\\Users\\USUARIO\\Desktop\\tarea interfaz\\tecnar.png")
icono = ImageTk.PhotoImage(path)
ventana_registro.iconphoto(True, icono)

image = Image.open("\\Users\\USUARIO\\Desktop\\tarea interfaz\\fondo.jpg")
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

Confirmacion = tkinter.Label(ventana_registro, text="", bd= 0,background="white")
Confirmacion.grid(row=8, column=0, padx=(50,0), pady=(20,0))






e1 = tkinter.Entry(ventana_registro)
e2 = tkinter.Entry(ventana_registro)
e3 = tkinter.Entry(ventana_registro)
e4 = tkinter.Entry(ventana_registro)


def obtener_estado():
    if variable1.get() == 1:
       Confirmacion.config(text="masculino",fg="white")
    if variable2.get() == 1:
       Confirmacion.config(text="femenino",fg="white")

    

variable1 = tkinter.IntVar()
variable2 = tkinter.IntVar()

casilla_masculino = tkinter.Checkbutton(ventana_registro, text="MASCULINO" ,variable=variable1 , command=obtener_estado)
casilla_femenino = tkinter.Checkbutton(ventana_registro, text="FEMENINO",variable=variable2, command= obtener_estado)



combo = ttk.Combobox(
    state="readonly",
    values=["Cartagena", "Barranquilla", "Bogota", "Medellin"]
)

def imprimir():
    
    entrada_nombre = e1.get()
    entrada_apellido = e2.get()
    entrada_edad = e3.get()
    entrada_direccion = e4.get()
    genero = Confirmacion["text"]
    seleccion = combo.get()
    
    

    messagebox.showinfo("REGISTRO EXITOSO","Nombre: "+ entrada_nombre + "\n" + "Apellido: " + entrada_apellido + "\n" + "Edad: " + entrada_edad + "\n" + "Direccion: " + entrada_direccion + "\n" + "Sexo: " + genero + "\n" + "Ciudad:  " + seleccion )

button = tkinter.Button(text="REGISTRARSE", command=imprimir)



e1.grid(row=1, column=1, padx=(50,0), pady=(160,0))
e2.grid(row=2, column=1, padx=(50,0), pady=(20,0))
e3.grid(row=3, column=1, padx=(50,0), pady=(20,0))
e4.grid(row=4, column=1, padx=(50,0), pady=(20,0))
casilla_masculino.grid(row=5, column=1, padx=(50,0), pady=(20,0))
casilla_femenino.grid(row=5, column=2, padx=(50,0), pady=(20,0))


combo.grid(row=6, column=1, padx=(50,0), pady=(20,0))
button.grid(row=7, column=1, padx=(50,0), pady=(50,0))

 

ventana_registro.mainloop()