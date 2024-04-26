import tkinter      #santiago Jimenez Ferrer
from PIL import Image, ImageTk


ventana= tkinter.Tk()
ventana.geometry("700x400")
ventana.title("PERSONALIZA EL TEXTO")
ventana.configure(background="lightblue")

path = Image.open("tecnar.png")
icono = ImageTk.PhotoImage(path)
ventana.iconphoto(True, icono)


image = Image.open("hola.png")
image = image.resize((200,200))

image = ImageTk.PhotoImage(image)

personaimagen = tkinter.Label(image=image,bd=0)
personaimagen.place(x=450,y=107)


textoori= tkinter.Label(ventana,text="CAMBIAME",background="white", font="consolas 15 bold",
                      relief=tkinter.GROOVE,bd=0, padx=10,pady=10)
textoori.pack(padx=30,pady=40)

cajatexto=tkinter.Entry(ventana,font="arial 15",bd=6)
cajatexto.place(x= 280 ,y=107, width=150)


def nuevo_texto():
  nuevo_text = cajatexto.get()
  textoori.config(text= nuevo_text)
  

boton1=tkinter.Button(ventana, text="CAMBIAR", font="consolas 15 bold",command=nuevo_texto)
boton1.place(x=300,y=150)

def borrar_texto():
  
 textoori.config(text= "")
 

boton2=tkinter.Button(ventana, text="BORRAR", font="consolas 15 bold",command=borrar_texto)
boton2.place(x=300,y=200)

boton3 = tkinter.Button(ventana, text="DESHABILITADO", state="disabled")
boton3.place(x=300,y=250)

def cambiar_color():
    seleccion = lista.curselection()
    for index in seleccion:
        color = lista.get(index)
        ventana.configure(background= color)
        


lista = tkinter.Listbox(ventana, width=30, selectmode="multiple")
lista.place(x=85,y=100)

elementos = ["RED", "BLUE", "GREY", "GREEN"]

for elemento in elementos:
    lista.insert(tkinter.END, elemento)

boton = tkinter.Button(ventana, text="CAMBIAR COLOR", command=cambiar_color)
boton.place(x=85,y=300)


ventana.mainloop()