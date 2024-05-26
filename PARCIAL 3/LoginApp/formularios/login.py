import tkinter as tk
import util.generic as utl
from tkinter import messagebox
import json
from tkinter import font

from formularios.PAdmin import PAdmin
from formularios.PVentas import PVentas

class Login(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("INGRESO AL SISTEMA")
        self.resizable(False, False)
        utl.centrar_ventana(self, 500, 500)
        self.logo = utl.leer_imagen("\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\imagenes\\ventana login.png", (500, 500))

        self.frame= tk.Frame(self, bd=0, width=500, height=500,relief=tk.SOLID)
        self.frame.place(x=0,y=0)
        self.fondo = tk.Label(self.frame,image= self.logo)
        self.fondo.place(x=0, y=0)

        self.entrada_usuario = tk.Entry(self.frame, font= ("Comic Sans MS", 14) ,bg="SlateBlue1", bd= 0)
        self.entrada_usuario.place(x= 210, y= 165, height= 25, width= 120)

        self.entrada_contraseña = tk.Entry(self.frame, font= ("Comic Sans MS", 14) ,bg="SlateBlue1", bd= 0,show="*")
        self.entrada_contraseña.place(x= 210, y= 240, height= 25, width= 120)

        self.bton_ingresar = tk.Button(self.frame,text= "INICIAR SESION", command= self.validar, bg="SlateBlue1", fg= "white", bd= 0, font= ("Comic Sans MS", 12))
        self.bton_ingresar.place(x = 175 , y= 325 ,width= 150)

    def validar(self):

        usuario = self.entrada_usuario.get()
        contraseña = self.entrada_contraseña.get()

        with open("\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\Usuarios.json", "r") as archivo:
            Usuarios = json.load(archivo)


        if usuario == "" and contraseña == "":

            messagebox.showerror('',"Campo Usuario / Contraseña vacio")
            self.entrada_usuario.focus()

        else:
            for usuarios in Usuarios["users"]:
                if usuario == usuarios["username"] and contraseña == usuarios["password"] and usuarios["role"] == "Administrador":
                    self.destroy()
                    PAdmin(usuarios["name"],usuarios["username"],usuarios["email"]).mainloop()
                elif usuario == usuarios["username"] and contraseña == usuarios["password"] and usuarios["role"] == "Vendedor":
                    self.destroy()
                    PVentas(usuarios["name"],usuarios["username"],usuarios["email"]).mainloop()
                


    
    

        