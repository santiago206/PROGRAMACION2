import tkinter

#ventana
ventana= tkinter.Tk()
ventana.geometry("700x400")
ventana.title("PERSONALIZA EL TEXTO")
ventana.configure(background="lightblue")

textoori= tkinter.Label(ventana,text="CAMBIAME",background="white", font="consolas 15 bold",
                      relief=tkinter.GROOVE,bd=0, padx=10,pady=10)
textoori.pack(padx=30,pady=40)

cajatexto=tkinter.Entry(ventana,font="arial 15",bd=6)
cajatexto.place(x= 280 ,y=107, width=150)


def cambiar_texto():
  nuevo_texto = cajatexto.get()
  textoori.config(text= nuevo_texto)
  

boton1=tkinter.Button(ventana, text="CAMBIAR", font="consolas 15 bold",command=cambiar_texto)
boton1.place(x=300,y=150)

def borrar_texto():
  
 textoori.config(text= "")

boton2=tkinter.Button(ventana, text="BORRAR", font="consolas 15 bold",command=borrar_texto)
boton2.place(x=300,y=200)

boton3 = tkinter.Button(ventana, text="DESHABILITADO", state="disabled")
boton3.place(x=300,y=250)

def obtener_seleccion():
    seleccionados = cuadro_lista.curselection()
    for index in seleccionados:
        elemento = cuadro_lista.get(index)
        ventana.configure(background= elemento)
        


cuadro_lista = tkinter.Listbox(ventana, width=30, selectmode="multiple")
cuadro_lista.place(x=85,y=100)

elementos = ["RED", "BLUE", "GREY", "GREEN"]

for elemento in elementos:
    cuadro_lista.insert(tkinter.END, elemento)

boton = tkinter.Button(ventana, text="Obtener", command=obtener_seleccion)
boton.place(x=85,y=300)





ventana.mainloop()