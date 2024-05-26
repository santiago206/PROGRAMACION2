import tkinter 
from PIL import Image, ImageTk
from tkinter import messagebox

ventana= tkinter.Tk()
ventana.geometry("800x500")
ventana.resizable(False,False)

primer_frame = tkinter.Frame(ventana,bg="gray",height="500",width="400")
primer_frame.place(x=0,y=0)


image = Image.open("\\Users\\Biblioteca\\Desktop\\actividad3\\logo.png")
image = image.resize((250,100))
image = ImageTk.PhotoImage(image)
inicio_imagen = tkinter.Label(image=image,bg="white")
inicio_imagen.place(x=70,y=100)

segundo_frame = tkinter.Frame(ventana,bg="white",height="500",width="400")
segundo_frame.place(x=400,y=0)

login_panel = tkinter.Label(ventana,text="INGRESAR",bg= "white",font= "arial 14")
login_panel.place(x= "500", y="80",width= "200")

login_usuario = tkinter.Label(ventana,text="USUARIO: ",bg= "white",font= "arial 14")
login_usuario.place(x= "430", y="140",width= "200")

login_CLAVE = tkinter.Label(ventana,text="CLAVE: ",bg= "white",font= "arial 14")
login_CLAVE.place(x= "420", y="200",width= "200")

entrada_usurio = tkinter.Entry(ventana, bg= "white",font= "arial 14",bd=4)
entrada_usurio.place(x= "600", y="140",width= "120")

entrada_clave = tkinter.Entry(ventana, bg= "white",font= "arial 14",bd=4)
entrada_clave.place(x= "600", y="200",width= "120")

def ingreso():
    
    user = entrada_usurio.get()
    contra = entrada_clave.get()
    
    if user == "" and contra == "":
        messagebox.showinfo("","CAMPOS VACIOS " + str(user))
    else:
        messagebox.showinfo("","BIENVENIDO " + str(user))
    

boton_ingresar = tkinter.Button(ventana,text="INGRESAR",bg= "white",font= "arial 14",bd=4,command=ingreso)
boton_ingresar.place(x= "550", y="300",width= "120")


ventana.mainloop()

