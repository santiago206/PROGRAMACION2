import tkinter as tk
import json
from tkinter import messagebox, ttk
import util.generic as utl
from tkinter import filedialog
from tkcalendar import DateEntry


class PAdmin(tk.Tk):
    def __init__(self, name="", username="", email=""):
        self.name = name
        self.username = username
        self.email = email
        super().__init__()
        self.title("Panel Administrativo")
        self.resizable(False, False)
        
        self.ancho_pantalla = self.winfo_screenwidth() 
        self.alto_pantalla = self.winfo_screenheight() 

        self.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}")
        
        menubar = tk.Menu(self)  
        menuuser = tk.Menu(menubar, tearoff=0 )
        menuuser.add_command(label="Crear Usuario", command=self.crear_usuario_form )
        menuuser.add_command(label="Listar - Eliminar - Actualizar", command=self.listar_eliminar_actualizar_usuarios)
        menubar.add_cascade(label="Usuarios", menu=menuuser)  

        menuclientes = tk.Menu(menubar, tearoff=0)
        menuclientes.add_command(label="Crear Cliente", command=self.crear_Cliente_form)  
        menuclientes.add_command(label="Listar - Eliminar - Actualizar",command=self.listar_eliminar_actualizar_clientes)
        
        menubar.add_cascade(label="Clientes", menu=menuclientes)

        menuventas = tk.Menu(menubar, tearoff=0)
        menuventas.add_command(label="Agregar Cancha", command=self.crear_cancha_form)
        menuventas.add_command(label="Listar - Eliminar - Actualizar", command=self.listar_eliminar_actualizar_canchas)
        menubar.add_cascade(label="Canchas", menu=menuventas)

        menucategorias = tk.Menu(menubar, tearoff=0)
        menucategorias.add_command(label="Crear Reserva", command=self.crear_reserva_form)  
        menucategorias.add_command(label="Listar - Eliminar - Actualizar" , command=self.listar_eliminar_actualizar_reservas)  
        menubar.add_cascade(label="Reservas", menu=menucategorias)   

        menuproducto = tk.Menu(menubar, tearoff=0)
        menuproducto.add_command(label="Crear Factura", command=self.crear_factura_form)  
        menuproducto.add_command(label="Listar - Eliminar - Actualizar", command= self.listar_eliminar_actualizar_facturas)  
        menubar.add_cascade(label="Facturacion", menu=menuproducto)   

        self.config(menu=menubar,bg="gray25")

        #####################       Apartado de Usuarios       #################################

        self.frame_user_info = tk.Frame(self, bd=0,relief=tk.SOLID, width=200,background= "gray25")
        self.frame_user_info.pack(side=tk.LEFT, padx=4, pady=5,fill="y")
        
        texto=tk.Label(self.frame_user_info, text="PANEL ADMINISTRATIVO", font= ("Comic Sans MS", 20, "bold") ,fg= "White" ,bg="gray25")
        texto.pack(padx=20,pady=4)
        self.usrimg = utl.leer_imagen("\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\imagenes\\logo user.png", (140, 140))
        self.imgusr=tk.Label(self.frame_user_info,image= self.usrimg , background= "gray25")
        self.imgusr.pack(padx=30,pady=4)
        texto1=tk.Label(self.frame_user_info, text=self.name, font= ("Comic Sans MS", 14),fg= "White" ,bg="gray25")
        texto1.pack(padx=40,pady=4)
        texto1=tk.Label(self.frame_user_info, text=self.email, font= ("Comic Sans MS", 14),fg= "White" ,bg="gray25")
        texto1.pack(padx=50,pady=4)
        
        #frame_data
        
        self.frame_data = tk.Frame(self, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_data.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)

        #frame_dinamyc
        self.frame_dinamyc = tk.Frame(self.frame_data, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}", bg= "white")
        self.frame_dinamyc.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)
        self.adminimg = utl.leer_imagen("\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\imagenes\\logo admin.png", (300, 300))
        self.admini=tk.Label(self.frame_dinamyc,image= self.adminimg , background= "white")
        self.admini.pack(pady= 150)
        

    def crear_usuario_form(self):

        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="REGISTRO DE USUARIOS", font= ("Comic Sans MS", 16 ,"bold") ,bg = "white")
        labelform.place(x=70, y=70)
        
        labelcedula = tk.Label(self.frame_dinamyc,text="Cedula:", font= ("Comic Sans MS", 14) ,bg = "white")
        labelcedula.place(x=70, y= 140)
        self.ccedula = tk.Entry(self.frame_dinamyc, width=80)
        self.ccedula.place(x=250, y=140)

        labelnombre = tk.Label(self.frame_dinamyc,text="Nombre completo:", font=("Comic Sans MS", 14) ,bg = "white")
        labelnombre.place(x=70, y=170)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=80)
        self.cnombre.place(x=250, y=170)

        labelusuario = tk.Label(self.frame_dinamyc,text="Username:", font=("Comic Sans MS", 14) ,bg = "white")
        labelusuario.place(x=70,y=200)
        self.cusuario = tk.Entry(self.frame_dinamyc, width=80)
        self.cusuario.place(x=250,y=200)

        labelclave = tk.Label(self.frame_dinamyc,text="Contraseña:", font=("Comic Sans MS", 14) ,bg = "white")
        labelclave.place(x=70,y= 230)
        self.cclave = tk.Entry(self.frame_dinamyc, width=80, show="*")
        self.cclave.place(x=250, y= 230)

        labelcorreo = tk.Label(self.frame_dinamyc,text="Correo:", font=("Comic Sans MS", 14) ,bg = "white")
        labelcorreo.place(x=70,y=260)
        self.ccorreo = tk.Entry(self.frame_dinamyc, width=80)
        self.ccorreo.place(x=250, y=260)

        labeltipo = tk.Label(self.frame_dinamyc, text="Tipo:", font= ("Comic Sans MS", 14) ,bg = "white")
        labeltipo.place(x=70,y=290)
        self.listatipo = tk.Listbox(self.frame_dinamyc, selectmode="Single", width=80, height=2)
        self.listatipo.place(x=250,y=290)
        self.listatipo.insert(1, "Administrador")
        self.listatipo.insert(2, "Vendedor")

        btnguardar = tk.Button(self.frame_dinamyc, text="GUARDAR", font= ("Comic Sans MS", 14, "bold"), command=self.save_user)
        btnguardar.place(x=250, y=340)

    def save_user(self):

        if self.ccedula.get() == "" or self.cnombre.get()== "" or  self.cusuario.get() == "" or self.cclave.get() == "" or self.ccorreo.get() == "" :
            messagebox.showerror("","Campos Vacios")
        else:
            for index in self.listatipo.curselection():
                tipo_user = self.listatipo.get(index)
                
            with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\Usuarios.json', "r", encoding='utf-8') as file:
                    Usuarios = json.load(file)
                    Usuarios["users"].append({
                            'id': self.ccedula.get(),
                            'name': self.cnombre.get(),
                            'username': self.cusuario.get(),
                            'password': self.cclave.get(),
                            'email': self.ccorreo.get(),
                            'role':tipo_user
                        })
                    with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\Usuarios.json', 'w') as jf: 
                        json.dump(Usuarios, jf, indent=4, ensure_ascii=True)
                        messagebox.showinfo('Info',"Usuario registrado con exito",parent=self)
                        
                        self.ccedula.delete(0, tk.END)
                        self.cnombre.delete(0, tk.END)
                        self.cusuario.delete(0, tk.END)
                        self.cclave.delete(0, tk.END)
                        self.ccorreo.delete(0, tk.END)
    
    def listar_eliminar_actualizar_usuarios(self):

        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="LISTADO DE USUARIOS", font= ("Comic Sans MS", 16 ,"bold") ,bg = "white")
        labelform.place(x=20, y=40)
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("NombreCompleto", "Username", "Email", "Rol"))
        self.tablausuarios.heading("#0", text="Cedula")
        self.tablausuarios.heading("NombreCompleto", text="Nombre Completo")
        self.tablausuarios.heading("Username", text="Usuario")
        self.tablausuarios.heading("Email", text="Email")
        self.tablausuarios.heading("Rol", text="Rol")
        with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\Usuarios.json', "r", encoding='utf-8') as file:
                Usuarios = json.load(file)
                for usuarios in Usuarios["users"]:
                    self.tablausuarios.insert("", "end", text=f'{usuarios["id"]}',values=(f'{usuarios["name"]}',f'{usuarios["username"]}',f'{usuarios["email"]}' ,f'{usuarios["role"]}'))
        self.tablausuarios.place(x=20, y= 90 ,width= 930)

        def eliminar_Usuario():

            try:
                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\Usuarios.json', 'r') as jf:
                    Usuarios = json.load(jf)
            except FileNotFoundError:
                Usuarios = {"users": []}
            
            selected_items = self.tablausuarios.selection()
            if not selected_items:
                messagebox.showwarning("Advertencia", "Seleccione un usuario para Eliminar")
                return
            
            global ids_to_delete
            ids_to_delete = []

            for item in selected_items:
                # Obtener el índice de cada item seleccionado
                item_index = self.tablausuarios.index(item)
                ids_to_delete.append(item_index)
                self.tablausuarios.delete(item)

            # Eliminar los usuarios seleccionados de la lista
            ids_to_delete.sort(reverse=True)  # Ordenar en orden descendente
            for item_index in ids_to_delete:
                del Usuarios["users"][item_index]

            # Actualizar el archivo JSON
            with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\Usuarios.json', 'w') as jf:
                json.dump(Usuarios, jf, indent=4)

                messagebox.showinfo("Información", "Usuario(s) eliminado(s)")
                
        
        labelcedula = tk.Label(self.frame_dinamyc,text="Cedula:", font= ("Comic Sans MS", 14) ,bg = "white")
        labelcedula.place(x=70, y= 340)
        self.ccedula = tk.Entry(self.frame_dinamyc, width=80)
        self.ccedula.place(x=250, y=340)

        labelnombre = tk.Label(self.frame_dinamyc,text="Nombre completo:", font=("Comic Sans MS", 14) ,bg = "white")
        labelnombre.place(x=70, y=370)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=80)
        self.cnombre.place(x=250, y=370)

        labelusuario = tk.Label(self.frame_dinamyc,text="Username:", font=("Comic Sans MS", 14) ,bg = "white")
        labelusuario.place(x=70,y=400)
        self.cusuario = tk.Entry(self.frame_dinamyc, width=80)
        self.cusuario.place(x=250,y= 400)

        labelclave = tk.Label(self.frame_dinamyc,text="Contraseña:", font=("Comic Sans MS", 14) ,bg = "white")
        labelclave.place(x=70,y= 430)
        self.cclave = tk.Entry(self.frame_dinamyc, width=80, show="*")
        self.cclave.place(x=250, y= 430)

        labelcorreo = tk.Label(self.frame_dinamyc,text="Correo:", font=("Comic Sans MS", 14) ,bg = "white")
        labelcorreo.place(x=70,y=460)
        self.ccorreo = tk.Entry(self.frame_dinamyc, width=80)
        self.ccorreo.place(x=250, y=460)

        labeltipo = tk.Label(self.frame_dinamyc, text="Tipo:", font= ("Comic Sans MS", 14) ,bg = "white")
        labeltipo.place(x=70,y=490)
        self.listatipo = tk.Listbox(self.frame_dinamyc, selectmode="Single", width=80, height=2)
        self.listatipo.place(x=250,y=490)
        self.listatipo.insert(1, "Administrador")
        self.listatipo.insert(2, "Vendedor")

        boton_eliminar = tk.Button(self.frame_dinamyc, text="Eliminar Usuario", command=eliminar_Usuario,font= ("Comic Sans MS", 14 ,"bold"))
        boton_eliminar.place(x= 70, y= 550)

        def actualizar_Usuario():

            eleccion_rol = False

            for index in self.listatipo.curselection():
                
                tipo_user = self.listatipo.get(index)
                eleccion_rol = True
                

            selected_items = self.tablausuarios.selection()  # Obtener los items seleccionados
            if not selected_items:
                messagebox.showwarning("Advertencia", "Seleccione un usuario para actualizar")
                return

            try:
                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\Usuarios.json', 'r') as jf:
                    Usuarios = json.load(jf)
            except FileNotFoundError:
                Usuarios = {"users": []}

            for item in selected_items:
                item_index = self.tablausuarios.index(item)

                # Obtener los nuevos datos, utilizando los valores actuales si los campos de entrada están vacíos
                nuevo_id = self.ccedula.get() or Usuarios["users"][item_index]["id"]
                nuevo_nombre = self.cnombre.get() or Usuarios["users"][item_index]["name"]
                nuevo_usuario = self.cusuario.get() or Usuarios["users"][item_index]["username"]
                nueva_clave = self.cclave.get() or Usuarios["users"][item_index]["password"]
                nuevo_correo = self.ccorreo.get() or Usuarios["users"][item_index]["email"]

                if eleccion_rol == False:
                    tipo_user = Usuarios["users"][item_index]["role"]
                else:
                    tipo_user = tipo_user

                nuevo_Rol = tipo_user

                # Actualizar el usuario en la lista de usuarios
                Usuarios["users"][item_index] = {
                    "id": nuevo_id,
                    "name": nuevo_nombre,
                    "username": nuevo_usuario,
                    "password": nueva_clave,
                    "email": nuevo_correo,
                    "role" : nuevo_Rol
                }
            
            with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\Usuarios.json', 'w') as jf:
                json.dump(Usuarios, jf, indent=4)

                messagebox.showinfo("Información", "Usuario actualizado")
                self.ccedula.delete(0, tk.END)
                self.cnombre.delete(0, tk.END)
                self.cusuario.delete(0, tk.END)
                self.cclave.delete(0, tk.END)
                self.ccorreo.delete(0, tk.END)


        btnactualizar = tk.Button(self.frame_dinamyc, text="ACTUALIZAR", font= ("Comic Sans MS", 14, "bold"),command= actualizar_Usuario)
        btnactualizar.place(x=250, y=550)

        


    #####################       Apartado de Clientes     #################################

    def crear_Cliente_form(self):

        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="REGISTRO DE CLIENTES", font= ("Comic Sans MS", 16 ,"bold") ,bg = "white")
        labelform.place(x=70, y=70)
        
        labelcedula = tk.Label(self.frame_dinamyc,text="Cedula:", font= ("Comic Sans MS", 14) ,bg = "white")
        labelcedula.place(x=70, y= 140)
        self.ccedula = tk.Entry(self.frame_dinamyc, width=80)
        self.ccedula.place(x=250, y=140)

        labelnombre = tk.Label(self.frame_dinamyc,text="Nombre completo:", font=("Comic Sans MS", 14) ,bg = "white")
        labelnombre.place(x=70, y=170)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=80)
        self.cnombre.place(x=250, y=170)

        labelusuario = tk.Label(self.frame_dinamyc,text="Username:", font=("Comic Sans MS", 14) ,bg = "white")
        labelusuario.place(x=70,y=200)
        self.cusuario = tk.Entry(self.frame_dinamyc, width=80)
        self.cusuario.place(x=250,y=200)

        labelclave = tk.Label(self.frame_dinamyc,text="Contraseña:", font=("Comic Sans MS", 14) ,bg = "white")
        labelclave.place(x=70,y= 230)
        self.cclave = tk.Entry(self.frame_dinamyc, width=80, show="*")
        self.cclave.place(x=250, y= 230)

        labelcorreo = tk.Label(self.frame_dinamyc,text="Correo:", font=("Comic Sans MS", 14) ,bg = "white")
        labelcorreo.place(x=70,y=260)
        self.ccorreo = tk.Entry(self.frame_dinamyc, width=80)
        self.ccorreo.place(x=250, y=260)

        btnguardar = tk.Button(self.frame_dinamyc, text="GUARDAR", font= ("Comic Sans MS", 14, "bold"), command=self.save_cliente)
        btnguardar.place(x=250, y=340)

    def save_cliente(self):
        
        if self.ccedula.get() == "" or self.cnombre.get()== "" or  self.cusuario.get() == "" or self.cclave.get() == "" or self.ccorreo.get() == "" :
            messagebox.showerror("","Campos Vacios")
        else:
                
            with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CLIENTES.json', "r", encoding='utf-8') as file:
                    clientes = json.load(file)
                    clientes["clientes"].append({
                            'id': self.ccedula.get(),
                            'name': self.cnombre.get(),
                            'username': self.cusuario.get(),
                            'password': self.cclave.get(),
                            'email': self.ccorreo.get()
                        })
                    with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CLIENTES.json', 'w') as jf: 
                        json.dump(clientes, jf, indent=4, ensure_ascii=True)
                        messagebox.showinfo('Info',"Cliente registrado con exito",parent=self)
                        
                        self.ccedula.delete(0, tk.END)
                        self.cnombre.delete(0, tk.END)
                        self.cusuario.delete(0, tk.END)
                        self.cclave.delete(0, tk.END)
                        self.ccorreo.delete(0, tk.END)

    def listar_eliminar_actualizar_clientes(self):

        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="LISTADO DE CLIENTES", font= ("Comic Sans MS", 16 ,"bold") ,bg = "white")
        labelform.place(x=20, y=40)
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("NombreCompleto", "Username", "Email"))
        self.tablausuarios.heading("#0", text="Cedula")
        self.tablausuarios.heading("NombreCompleto", text="Nombre Completo")
        self.tablausuarios.heading("Username", text="Usuario")
        self.tablausuarios.heading("Email", text="Email")
        with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CLIENTES.json', "r", encoding='utf-8') as file:
                clientes = json.load(file)
                for clien in clientes["clientes"]:
                    self.tablausuarios.insert("", "end", text=f'{clien["id"]}',values=(f'{clien["name"]}',f'{clien["username"]}',f'{clien["email"]}'))
        self.tablausuarios.place(x=20, y= 90 ,width= 930)

        def eliminar_Usuario():

            try:
                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CLIENTES.json', 'r') as jf:
                    clientes = json.load(jf)
            except FileNotFoundError:
                clientes = {"users": []}
            
            selected_items = self.tablausuarios.selection()
            if not selected_items:
                messagebox.showwarning("Advertencia", "Seleccione uno o varios clientes para Eliminar")
                return
            
            global ids_to_delete
            ids_to_delete = []

            for item in selected_items:
                # Obtener el índice de cada item seleccionado
                item_index = self.tablausuarios.index(item)
                ids_to_delete.append(item_index)
                self.tablausuarios.delete(item)

            # Eliminar los usuarios seleccionados de la lista
            ids_to_delete.sort(reverse=True)  # Ordenar en orden descendente
            for item_index in ids_to_delete:
                del clientes["clientes"][item_index]

            # Actualizar el archivo JSON
            with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CLIENTES.json', 'w') as jf:
                json.dump(clientes, jf, indent=4)

                messagebox.showinfo("Información", "Cliente(s) eliminado(s)")
        
        labelcedula = tk.Label(self.frame_dinamyc,text="Cedula:", font= ("Comic Sans MS", 14) ,bg = "white")
        labelcedula.place(x=70, y= 340)
        self.ccedula = tk.Entry(self.frame_dinamyc, width=80)
        self.ccedula.place(x=250, y=340)

        labelnombre = tk.Label(self.frame_dinamyc,text="Nombre completo:", font=("Comic Sans MS", 14) ,bg = "white")
        labelnombre.place(x=70, y=370)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=80)
        self.cnombre.place(x=250, y=370)

        labelusuario = tk.Label(self.frame_dinamyc,text="Username:", font=("Comic Sans MS", 14) ,bg = "white")
        labelusuario.place(x=70,y=400)
        self.cusuario = tk.Entry(self.frame_dinamyc, width=80)
        self.cusuario.place(x=250,y= 400)

        labelclave = tk.Label(self.frame_dinamyc,text="Contraseña:", font=("Comic Sans MS", 14) ,bg = "white")
        labelclave.place(x=70,y= 430)
        self.cclave = tk.Entry(self.frame_dinamyc, width=80, show="*")
        self.cclave.place(x=250, y= 430)

        labelcorreo = tk.Label(self.frame_dinamyc,text="Correo:", font=("Comic Sans MS", 14) ,bg = "white")
        labelcorreo.place(x=70,y=460)
        self.ccorreo = tk.Entry(self.frame_dinamyc, width=80)
        self.ccorreo.place(x=250, y=460)

        boton_eliminar = tk.Button(self.frame_dinamyc, text="Eliminar Cliente", command=eliminar_Usuario,font= ("Comic Sans MS", 14 ,"bold"))
        boton_eliminar.place(x= 70, y= 550)

        def actualizar_Usuario():

            selected_items = self.tablausuarios.selection()  # Obtener los items seleccionados
            if not selected_items:
                messagebox.showwarning("Advertencia", "Seleccione un Cliente para actualizar")
                return

            try:
                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CLIENTES.json', 'r') as jf:
                    clientes = json.load(jf)
            except FileNotFoundError:
                clientes = {"clientes": []}

            for item in selected_items:
                item_index = self.tablausuarios.index(item)

                # Obtener los nuevos datos, utilizando los valores actuales si los campos de entrada están vacíos
                nuevo_id = self.ccedula.get() or  clientes["clientes"][item_index]["id"]
                nuevo_nombre = self.cnombre.get() or  clientes["clientes"][item_index]["name"]
                nuevo_usuario = self.cusuario.get() or clientes["clientes"][item_index]["username"]
                nueva_clave = self.cclave.get() or clientes["clientes"][item_index]["password"]
                nuevo_correo = self.ccorreo.get() or clientes["clientes"][item_index]["email"]

                # Actualizar el usuario en la lista de usuarios
                clientes["clientes"][item_index] = {
                    "id": nuevo_id,
                    "name": nuevo_nombre,
                    "username": nuevo_usuario,
                    "password": nueva_clave,
                    "email": nuevo_correo
                }
            
            with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CLIENTES.json', 'w') as jf:
                json.dump(clientes, jf, indent=4)

                messagebox.showinfo("Información", "Cliente actualizado")


        btnactualizar = tk.Button(self.frame_dinamyc, text="ACTUALIZAR", font= ("Comic Sans MS", 14, "bold"),command= actualizar_Usuario)
        btnactualizar.place(x=250, y=550)


    #####################       Apartado de Canchas           #################################
    
    def crear_cancha_form(self):

        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="REGISTRO DE CANCHAS", font= ("Comic Sans MS", 16 ,"bold") ,bg = "white")
        labelform.place(x=70, y=70)
        
        labelsuelo = tk.Label(self.frame_dinamyc,text="Nombre:", font= ("Comic Sans MS", 14) ,bg = "white")
        labelsuelo.place(x=70, y= 140)
        self.nombre = tk.Entry(self.frame_dinamyc, width=80)
        self.nombre.place(x= 250, y= 140)

        labeltamaño = tk.Label(self.frame_dinamyc,text="Tamaño:", font=("Comic Sans MS", 14) ,bg = "white")
        labeltamaño.place(x=70, y=170)

        self.tamaño = tk.Entry(self.frame_dinamyc, width=80)
        self.tamaño.place(x= 250, y= 170)
    
        labelusuario = tk.Label(self.frame_dinamyc,text="Direccion:", font=("Comic Sans MS", 14) ,bg = "white")
        labelusuario.place(x=70,y=200)
        self.cusuario = tk.Entry(self.frame_dinamyc, width=80)
        self.cusuario.place(x=250,y=200)

        labelclave = tk.Label(self.frame_dinamyc,text="Deporte:", font=("Comic Sans MS", 14) ,bg = "white")
        labelclave.place(x=70,y= 230)
        self.cclave = tk.Entry(self.frame_dinamyc, width=80)
        self.cclave.place(x=250, y= 230)

        labelprecio = tk.Label(self.frame_dinamyc,text="Precio:", font=("Comic Sans MS", 14) ,bg = "white")
        labelprecio.place(x=70,y= 260)
        self.pprecio = tk.Entry(self.frame_dinamyc, width=80)
        self.pprecio.place(x=250, y= 260)

        labelcorreo = tk.Label(self.frame_dinamyc,text="Imagen:", font=("Comic Sans MS", 14) ,bg = "white")
        labelcorreo.place(x=70,y=290)

        def Abrir_Archivo():
            global direccion
            direccion = filedialog.askopenfilename()
            print(direccion)

        self.abrir = tk.Button(self.frame_dinamyc, text= "Cargar Imagen" , command=Abrir_Archivo)
        self.abrir.place(x=250, y=290)

        btnguardar = tk.Button(self.frame_dinamyc, text="GUARDAR", font= ("Comic Sans MS", 14, "bold"), command= self.save_cancha)
        btnguardar.place(x=250, y=370)

    def save_cancha(self):

        
            if self.nombre.get() == "" or self.tamaño.get()== "" or  self.cusuario.get() == "" or self.cclave.get() == "" :
                messagebox.showerror("","Campos Vacios")
            else:

                    
                with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CANCHAS.json', "r", encoding='utf-8') as file:
                        canchas = json.load(file)

                        canchas["canchas"].append({
                                'Nombre de la cancha': self.nombre.get(),
                                'Longitud': self.tamaño.get(),
                                'Direccion': self.cusuario.get(),
                                'Deporte': self.cclave.get(),
                                'Precio' : self.pprecio.get(),
                                'Imagen': direccion
                            })
                        with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CANCHAS.json', 'w') as jf: 
                            json.dump(canchas, jf, indent=4, ensure_ascii=True)
                            messagebox.showinfo('Info',"Cancha registrada con exito",parent=self)
                            
                            self.nombre.delete(0, tk.END)
                            self.tamaño.delete(0, tk.END)
                            self.cusuario.delete(0, tk.END)
                            self.cclave.delete(0, tk.END)
                            self.pprecio.delete(0, tk.END)

    def listar_eliminar_actualizar_canchas(self):

        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="LISTADO DE CANCHAS", font= ("Comic Sans MS", 16 ,"bold") ,bg = "white")
        labelform.place(x=20, y=40)
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("Longitud", "Direccion", "Deporte","Precio","Imagen"))
        self.tablausuarios.heading("#0", text="Nombre")
        self.tablausuarios.heading("Longitud", text="Longitud")
        self.tablausuarios.heading("Direccion", text="Direccion")
        self.tablausuarios.heading("Deporte", text="Deporte")
        self.tablausuarios.heading("Precio", text="Precio")
        self.tablausuarios.heading("Imagen", text="Imagen")
        with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CANCHAS.json', "r", encoding='utf-8') as file:
                canchas = json.load(file)
                for canc in canchas["canchas"]:
                    self.tablausuarios.insert("", "end", text=f'{canc["Nombre de la cancha"]}',values=(f'{canc["Longitud"]}',f'{canc["Direccion"]}',f'{canc["Deporte"]}',f'{canc["Precio"]}',f'{canc["Imagen"]}'))
        self.tablausuarios.place(x=20, y= 90 ,width= 930)

        def eliminar_cancha():

            try:
                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CANCHAS.json', 'r') as jf:
                    canchas = json.load(jf)
            except FileNotFoundError:
                canchas = {"canchas": []}
            
            selected_items = self.tablausuarios.selection()
            if not selected_items:
                messagebox.showwarning("Advertencia", "Seleccione una o varias canchas para Eliminar")
                return
            
            global ids_to_delete
            ids_to_delete = []

            for item in selected_items:
                # Obtener el índice de cada item seleccionado
                item_index = self.tablausuarios.index(item)
                ids_to_delete.append(item_index)
                self.tablausuarios.delete(item)

            # Eliminar los usuarios seleccionados de la lista
            ids_to_delete.sort(reverse=True)  # Ordenar en orden descendente
            for item_index in ids_to_delete:
                del canchas["canchas"][item_index]

            # Actualizar el archivo JSON
            with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CANCHAS.json', 'w') as jf:
                json.dump(canchas, jf, indent=4)

                messagebox.showinfo("Información", "Cliente(s) eliminado(s)")
        
        labelcedula = tk.Label(self.frame_dinamyc,text="Nombre:", font= ("Comic Sans MS", 14) ,bg = "white")
        labelcedula.place(x=70, y= 340)
        self.ccedula = tk.Entry(self.frame_dinamyc, width=80)
        self.ccedula.place(x=250, y=340)

        labelnombre = tk.Label(self.frame_dinamyc,text="Tamaño:", font=("Comic Sans MS", 14) ,bg = "white")
        labelnombre.place(x=70, y=370)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=80)
        self.cnombre.place(x=250, y=370)

        labelusuario = tk.Label(self.frame_dinamyc,text="Direccion:", font=("Comic Sans MS", 14) ,bg = "white")
        labelusuario.place(x=70,y=400)
        self.cusuario = tk.Entry(self.frame_dinamyc, width=80)
        self.cusuario.place(x=250,y= 400)

        labelclave = tk.Label(self.frame_dinamyc,text="Deporte:", font=("Comic Sans MS", 14) ,bg = "white")
        labelclave.place(x=70,y= 430)
        self.cclave = tk.Entry(self.frame_dinamyc, width=80)
        self.cclave.place(x=250, y= 430)

        labelprecio = tk.Label(self.frame_dinamyc,text="Precio:", font=("Comic Sans MS", 14) ,bg = "white")
        labelprecio.place(x=70,y= 460)
        self.pprecio = tk.Entry(self.frame_dinamyc, width=80)
        self.pprecio.place(x=250, y= 460)

        labelcorreo = tk.Label(self.frame_dinamyc,text="Imagen:", font=("Comic Sans MS", 14) ,bg = "white")
        labelcorreo.place(x=70,y=490)

        abrir_imagen = False

        def Abrir_Archivo():
                global direccion
                direccion = filedialog.askopenfilename()
                print(direccion)
                global abrir_imagen
                abrir_imagen = True

        self.abrir = tk.Button(self.frame_dinamyc, text= "Cargar Imagen" , command=Abrir_Archivo)
        self.abrir.place(x=250, y=490)


        boton_eliminar = tk.Button(self.frame_dinamyc, text="Eliminar Cancha", command=eliminar_cancha,font= ("Comic Sans MS", 14 ,"bold"))
        boton_eliminar.place(x= 70, y= 550)

        def actualizar_cancha():


            selected_items = self.tablausuarios.selection()  # Obtener los items seleccionados
            if not selected_items:
                messagebox.showwarning("Advertencia", "Seleccione una cancha para actualizar")
                return

            try:
                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CANCHAS.json', 'r') as jf:
                    global canchas
                    canchas = json.load(jf)
            except FileNotFoundError:
                canchas = {"canchas": []}

            for item in selected_items:
                item_index = self.tablausuarios.index(item)

                # Obtener los nuevos datos, utilizando los valores actuales si los campos de entrada están vacíos
                nuevo_nombre = self.ccedula.get() or  canchas["canchas"][item_index]["Nombre de la cancha"]
                nuevo_tamaño = self.cnombre.get() or  canchas["canchas"][item_index]["Longitud"]
                nuevo_direccion = self.cusuario.get() or canchas["canchas"][item_index]["Direccion"]
                nueva_deporte = self.cclave.get() or canchas["canchas"][item_index]["Deporte"]
                nuevo_precio = self.pprecio.get() or canchas["canchas"][item_index]["Precio"]

                if abrir_imagen == False:
                    direccion = canchas["canchas"][item_index]["Imagen"]
                else:
                    direccion = direccion 

                # Actualizar el usuario en la lista de usuarios
                canchas["canchas"][item_index] = {
                    "Nombre de la cancha": nuevo_nombre,
                    "Longitud": nuevo_tamaño,
                    "Direccion": nuevo_direccion,
                    "Deporte": nueva_deporte,
                    "Precio": nuevo_precio,
                    "Imagen": direccion
                }
            
            with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CANCHAS.json', 'w') as jf:
                json.dump(canchas, jf, indent=4)

                messagebox.showinfo("Información", "Cancha actualizada")


        btnactualizar = tk.Button(self.frame_dinamyc, text="ACTUALIZAR", font= ("Comic Sans MS", 14, "bold"),command= actualizar_cancha)
        btnactualizar.place(x=250, y=550)


    ########################################            RESERVAS             ################################################

    def on_selection(self, event):
        selection = self.combo_cliente.get()
        print(selection)
        

    def cancha_selection(self, event):
        selection = self.combo_cancha.get()
        

    def horario_selection(self, event):
        selection = self.combo_horario.get()

    def print_selected_date(self,event):
        selected_date = self.fecha.get()
        print(f"Fecha seleccionada: {selected_date}")


    def crear_reserva_form(self):

        with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CLIENTES.json', 'r') as jf:
            clientes = json.load(jf)

        with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CANCHAS.json', 'r') as jf:
            canchas = json.load(jf)
        
        opciones_clientes = [clien["name"] for clien in clientes["clientes"]]
        opciones_canchas = [can["Nombre de la cancha"] for can in canchas["canchas"]]
            

        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="REGISTRO DE RESERVAS", font= ("Comic Sans MS", 16 ,"bold") ,bg = "white")
        labelform.place(x=70, y=70)
        
        labelcedula = tk.Label(self.frame_dinamyc,text="Cliente:", font= ("Comic Sans MS", 14) ,bg = "white")
        labelcedula.place(x=70, y= 140)

        self.combo_cliente = ttk.Combobox(self.frame_dinamyc,
                                        
            state="readonly",
            values= opciones_clientes
        )
        self.combo_cliente.place(x= 250, y=140)
        self.combo_cliente.bind("<<ComboboxSelected>>", self.on_selection)

        labelnombre = tk.Label(self.frame_dinamyc,text="Cancha:", font=("Comic Sans MS", 14) ,bg = "white")
        labelnombre.place(x=70, y=170)

        self.combo_cancha = ttk.Combobox(self.frame_dinamyc,
                                        
            state="readonly",
            values= opciones_canchas
        )
        self.combo_cancha.place(x= 250, y=170)
        self.combo_cancha.bind("<<ComboboxSelected>>", self.cancha_selection)

        labelusuario = tk.Label(self.frame_dinamyc,text="Fecha:", font=("Comic Sans MS", 14) ,bg = "white")
        labelusuario.place(x=70,y=200)

        self.fecha = DateEntry(self.frame_dinamyc, width=16, background='darkblue', foreground='white', borderwidth=2)
        self.fecha.place(x=250,y= 200)
        self.fecha.bind("<<DateEntrySelected>>", self.print_selected_date)

        labelclave = tk.Label(self.frame_dinamyc,text="Hora:", font=("Comic Sans MS", 14) ,bg = "white")
        labelclave.place(x=70,y= 230)
        self.hora = tk.Entry(self.frame_dinamyc, width=80)
        self.hora.place(x=250, y= 230)

        labelharario = tk.Label(self.frame_dinamyc,text="Horario:", font=("Comic Sans MS", 14) ,bg = "white")
        labelharario.place(x=70,y= 260)

        self.combo_horario = ttk.Combobox(self.frame_dinamyc,
                                        
            state="readonly",
            values= ["Dia","Noche"]
        )

        self.combo_horario.place(x= 250, y=260)
        self.combo_horario.bind("<<ComboboxSelected>>", self.horario_selection)
        
        btnguardar = tk.Button(self.frame_dinamyc, text="GUARDAR", font= ("Comic Sans MS", 14, "bold"), command=self.save_reserva)
        btnguardar.place(x=250, y=340)

    def save_reserva(self):

        
            if self.combo_cliente.get() == "" or self.combo_cancha.get()== "" or  self.fecha.get() == "" or self.hora.get() == "" or self.combo_horario.get() == "" :
                messagebox.showerror("","Campos Vacios")
            else:

                    
                with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\RESERVAS.json', "r", encoding='utf-8') as file:
                        reservas = json.load(file)

                        reservas["reservas"].append({
                                'cliente': self.combo_cliente.get(),
                                'cancha': self.combo_cancha.get(),
                                'fecha': self.fecha.get(),
                                'hora': self.hora.get(),
                                'horario': self.combo_horario.get()
                            })
                        with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\RESERVAS.json', 'w') as jf: 
                            json.dump(reservas, jf, indent=4, ensure_ascii=True)
                            messagebox.showinfo('Info',"Reserva registrada con exito",parent=self)
                            
                            self.fecha.delete(0, tk.END)
                            self.hora.delete(0, tk.END)

    
    def listar_eliminar_actualizar_reservas(self):

        with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CLIENTES.json', 'r') as jf:
            clientes = json.load(jf)

        with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CANCHAS.json', 'r') as jf:
            canchas = json.load(jf)
        
        opciones_clientes = [clien["name"] for clien in clientes["clientes"]]
        opciones_canchas = [can["Nombre de la cancha"] for can in canchas["canchas"]]

        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="LISTADO DE RESERVAS", font= ("Comic Sans MS", 16 ,"bold") ,bg = "white")
        labelform.place(x=20, y=40)
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("Cancha", "Fecha", "Hora","Horario"))
        self.tablausuarios.heading("#0", text="Cliente")
        self.tablausuarios.heading("Cancha", text="Cancha")
        self.tablausuarios.heading("Fecha", text="Fecha")
        self.tablausuarios.heading("Hora", text="Hora")
        self.tablausuarios.heading("Horario", text="Horario")
        with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\RESERVAS.json', "r", encoding='utf-8') as file:
                reservas = json.load(file)
                for reser in reservas["reservas"]:
                    self.tablausuarios.insert("", "end", text=f'{reser["cliente"]}',values=(f'{reser["cancha"]}',f'{reser["fecha"]}',f'{reser["hora"]}',f'{reser["horario"]}'))
        self.tablausuarios.place(x=20, y= 90 ,width= 930)

        def eliminar_reserva():

            try:
                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\RESERVAS.json', 'r') as jf:
                    reservas = json.load(jf)
            except FileNotFoundError:
                reservas = {"reservas": []}
            
            selected_items = self.tablausuarios.selection()
            if not selected_items:
                messagebox.showwarning("Advertencia", "Seleccione una o varias reservas para Eliminar")
                return
            
            global ids_to_delete
            ids_to_delete = []

            for item in selected_items:
                # Obtener el índice de cada item seleccionado
                item_index = self.tablausuarios.index(item)
                ids_to_delete.append(item_index)
                self.tablausuarios.delete(item)

            # Eliminar los usuarios seleccionados de la lista
            ids_to_delete.sort(reverse=True)  # Ordenar en orden descendente
            for item_index in ids_to_delete:
                del reservas["reservas"][item_index]

            # Actualizar el archivo JSON
            with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\RESERVAS.json', 'w') as jf:
                json.dump(reservas, jf, indent=4)

                messagebox.showinfo("Información", "Reserva(s) eliminada(s)")
        
        labelcedula = tk.Label(self.frame_dinamyc,text="Cliente:", font= ("Comic Sans MS", 14) ,bg = "white")
        labelcedula.place(x=70, y= 340)

        self.combo_cliente = ttk.Combobox(self.frame_dinamyc,
                                        
            state="readonly",
            values= opciones_clientes
        )
        self.combo_cliente.place(x= 250, y=340)
        self.combo_cliente.bind("<<ComboboxSelected>>", self.on_selection)

        labelnombre = tk.Label(self.frame_dinamyc,text="Cancha:", font=("Comic Sans MS", 14) ,bg = "white")
        labelnombre.place(x=70, y=370)

        self.combo_cancha = ttk.Combobox(self.frame_dinamyc,
                                        
            state="readonly",
            values= opciones_canchas
        )
        self.combo_cancha.place(x= 250, y=370)
        self.combo_cancha.bind("<<ComboboxSelected>>", self.cancha_selection)
        
        labelusuario = tk.Label(self.frame_dinamyc,text="Fecha:", font=("Comic Sans MS", 14) ,bg = "white")
        labelusuario.place(x=70,y=400)

        self.fecha = DateEntry(self.frame_dinamyc, width=16, background='darkblue', foreground='white', borderwidth=2)
        self.fecha.place(x=250,y= 400)
        self.fecha.bind("<<DateEntrySelected>>", self.print_selected_date)

    
        labelclave = tk.Label(self.frame_dinamyc,text="Hora:", font=("Comic Sans MS", 14) ,bg = "white")
        labelclave.place(x=70,y= 430)
        self.hora = tk.Entry(self.frame_dinamyc, width=80)
        self.hora.place(x=250, y= 430)

        labelcorreo = tk.Label(self.frame_dinamyc,text="Horario:", font=("Comic Sans MS", 14) ,bg = "white")
        labelcorreo.place(x=70,y=460)

        self.combo_horario = ttk.Combobox(self.frame_dinamyc,
                                        
            state="readonly",
            values= ["Dia","Noche"]
        )

        self.combo_horario.place(x= 250, y=460)
        self.combo_horario.bind("<<ComboboxSelected>>", self.horario_selection)
        

        boton_eliminar = tk.Button(self.frame_dinamyc, text="Eliminar Reserva", command=eliminar_reserva,font= ("Comic Sans MS", 14 ,"bold"))
        boton_eliminar.place(x= 70, y= 550)

        def actualizar_Reserva():

            selected_items = self.tablausuarios.selection()  # Obtener los items seleccionados
            if not selected_items:
                messagebox.showwarning("Advertencia", "Seleccione un Cliente para actualizar")
                return

            try:
                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\RESERVAS.json', 'r') as jf:
                    reservas = json.load(jf)
            except FileNotFoundError:
                reservas = {"reservas": []}

            for item in selected_items:
                item_index = self.tablausuarios.index(item)

                # Obtener los nuevos datos, utilizando los valores actuales si los campos de entrada están vacíos
                nuevo_cliente = self.combo_cliente.get() or  reservas["reservas"][item_index]["cliente"]
                nuevo_cancha = self.combo_cancha.get() or  reservas["reservas"][item_index]["cancha"]
                nuevo_fecha = self.fecha.get() or reservas["reservas"][item_index]["fecha"]
                nueva_hora = self.hora.get() or reservas["reservas"][item_index]["hora"]
                nuevo_horario = self.combo_horario.get() or reservas["reservas"][item_index]["horario"]

                # Actualizar el usuario en la lista de usuarios
                reservas["reservas"][item_index] = {
                    "cliente": nuevo_cliente,
                    "cancha": nuevo_cancha,
                    "fecha": nuevo_fecha,
                    "hora": nueva_hora,
                    "horario": nuevo_horario
                }
            
            with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\RESERVAS.json', 'w') as jf:
                json.dump(reservas, jf, indent=4)

                messagebox.showinfo("Información", "Reserva actualizada")


        btnactualizar = tk.Button(self.frame_dinamyc, text="ACTUALIZAR", font= ("Comic Sans MS", 14, "bold"),command= actualizar_Reserva)
        btnactualizar.place(x=250, y=550)

    ##############################################    FACTURAcION    ####################################################
                            
    def crear_factura_form(self):

        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="FACTURACION", font= ("Comic Sans MS", 16 ,"bold") ,bg = "white")
        labelform.place(x=70, y= 70)
        
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("Cancha", "Fecha", "Hora","Horario"))
        self.tablausuarios.heading("#0", text="Cliente")
        self.tablausuarios.heading("Cancha", text="Cancha")
        self.tablausuarios.heading("Fecha", text="Fecha")
        self.tablausuarios.heading("Hora", text="Hora")
        self.tablausuarios.heading("Horario", text="Horario")
        with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\RESERVAS.json', "r", encoding='utf-8') as file:
                reservas = json.load(file)
                for reser in reservas["reservas"]:
                    self.tablausuarios.insert("", "end", text=f'{reser["cliente"]}',values=(f'{reser["cancha"]}',f'{reser["fecha"]}',f'{reser["hora"]}',f'{reser["horario"]}'))
        self.tablausuarios.place(x=20, y= 135 ,width= 930)

        label_iva = tk.Label(self.frame_dinamyc, text="IVA", font= ("Comic Sans MS", 14, "bold"))
        label_iva.place(x=70, y= 410)

        self.entrada_iva = tk.Entry(self.frame_dinamyc, bg="white")
        self.entrada_iva.place(x=250, y= 410)

        btnguardar = tk.Button(self.frame_dinamyc, text="CREAR FACTURA", font= ("Comic Sans MS", 12, "bold"), command= self.save_factura)
        btnguardar.place(x=70, y= 500)


    def save_factura(self):
            
        
            with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CANCHAS.json', 'r') as jf:
                canchas = json.load(jf)
            
            with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\FACTURA.json', 'r') as jf:
                factura = json.load(jf)
            
            selected_items = self.tablausuarios.selection()
            if not selected_items:
                messagebox.showwarning("Advertencia", "Seleccione una o varias reservas para Eliminar")
                return

            try:
                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\RESERVAS.json', 'r') as jf:
                        reservas = json.load(jf)
            except FileNotFoundError:
                    reservas = {"reservas": []}
            
            for item in selected_items:
                    item_index = self.tablausuarios.index(item)

                    # Obtener los nuevos datos, utilizando los valores actuales si los campos de entrada están vacíos
                    cliente = reservas["reservas"][item_index]["cliente"]
                    cancha = reservas["reservas"][item_index]["cancha"]
                    fecha = reservas["reservas"][item_index]["fecha"]
                    hora = reservas["reservas"][item_index]["hora"]
                    horario = reservas["reservas"][item_index]["horario"]

                    precio = canchas["canchas"][item_index]["Precio"]

                    
                    factura["facturas"].append( {
                        "cliente": cliente,
                        "cancha": cancha,
                        "fecha": fecha,
                        "hora": hora,
                        "horario": horario,
                        "iva": self.entrada_iva.get(),
                        "precio": precio
                    
                    })
                
                    with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\FACTURA.json', 'w') as jf:
                        json.dump(factura, jf, indent=4)

                        messagebox.showinfo("Información", "Factura Creada")
                                
            def Descargar_factura():

                nombre =  cliente

                ruta_predeterminada = "\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\Facturas\\Factura " + nombre +".txt"

                with open(ruta_predeterminada, "w") as file:
                    file.write("#################     FACTURA       ###############" +"\n")
                    file.write( "Nombre del cliente: " + cliente +"\n")
                    file.write( "Nombre de la cancha: " + cancha +"\n")
                    file.write( "Fecha: " + fecha +"\n")
                    file.write( "Hora: " + hora +"\n")
                    file.write( "Horario: " + horario +"\n")
                    file.write( "Iva: " + self.entrada_iva.get() +"\n")
                    file.write( "Precio: " + precio +"\n")

                    iva = float(self.entrada_iva.get())
                    precio_con_iva = int(precio) * (1 +  (iva / 100))
                    file.write( "Total a Pagar: " + str(precio_con_iva) )

                print(f"Archivo guardado en: {ruta_predeterminada}")
                messagebox.showinfo("","Factura Descargada")

            btndescargar = tk.Button(self.frame_dinamyc, text="DESCARGAR FACTURA", font= ("Comic Sans MS", 12, "bold"),command=Descargar_factura)
            btndescargar.place(x= 250, y= 500)

    def listar_eliminar_actualizar_facturas(self):
        
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="LISTADO DE FACTURAS", font= ("Comic Sans MS", 16 ,"bold") ,bg = "white")
        labelform.place(x=70, y= 70)
        
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("Cancha", "Fecha", "Hora","Horario","Iva","Precio"))
        self.tablausuarios.heading("#0", text="Cliente")
        self.tablausuarios.heading("Cancha", text="Cancha")
        self.tablausuarios.heading("Fecha", text="Fecha")
        self.tablausuarios.heading("Hora", text="Hora")
        self.tablausuarios.heading("Horario", text="Horario")
        self.tablausuarios.heading("Iva", text="Iva")
        self.tablausuarios.heading("Precio", text="Precio")
        with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\FACTURA.json', "r", encoding='utf-8') as file:
                facturas = json.load(file)
                for fa in facturas["facturas"]:
                    self.tablausuarios.insert("", "end", text=f'{fa["cliente"]}',values=(f'{fa["cancha"]}',f'{fa["fecha"]}',f'{fa["hora"]}',f'{fa["horario"]}',f'{fa["iva"]}',f'{fa["precio"]}'))
        self.tablausuarios.place(x=20, y= 135 ,width= 930)

        label_iva = tk.Label(self.frame_dinamyc, text="IVA", font= ("Comic Sans MS", 14, "bold"))
        label_iva.place(x=70, y= 400)

        self.entrada_iva = tk.Entry(self.frame_dinamyc, bg="white")
        self.entrada_iva.place(x=250, y= 400)

        def eliminar_factura():

            try:
                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\FACTURA.json', 'r') as jf:
                    facturas = json.load(jf)
            except FileNotFoundError:
                facturas = {"reservas": []}
            
            selected_items = self.tablausuarios.selection()
            if not selected_items:
                messagebox.showwarning("Advertencia", "Seleccione una o varias facturas para Eliminar")
                return
            
            global ids_to_delete
            ids_to_delete = []

            for item in selected_items:
                # Obtener el índice de cada item seleccionado
                item_index = self.tablausuarios.index(item)
                ids_to_delete.append(item_index)
                self.tablausuarios.delete(item)

            # Eliminar los usuarios seleccionados de la lista
            ids_to_delete.sort(reverse=True)  # Ordenar en orden descendente
            for item_index in ids_to_delete:
                del facturas["facturas"][item_index]

            # Actualizar el archivo JSON
            with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\FACTURA.json', 'w') as jf:
                json.dump(facturas, jf, indent=4)

                messagebox.showinfo("Información", "Factura(s) eliminada(s)")
            
        boton_eliminar = tk.Button(self.frame_dinamyc, text="Eliminar Factura", command=eliminar_factura,font= ("Comic Sans MS", 14 ,"bold"))
        boton_eliminar.place(x= 70, y= 550)

        def actualizar_Factura():

            selected_items = self.tablausuarios.selection()
            if not selected_items:
                messagebox.showwarning("Advertencia", "Seleccione una Fcatura para Actualizar")
                return
            try:
                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\FACTURA.json', 'r') as jf:
                        facturas = json.load(jf)
            except FileNotFoundError:
                    facturas = {"factura": []}
            
            for item in selected_items:
                    item_index = self.tablausuarios.index(item)

                    # Obtener los nuevos datos, utilizando los valores actuales si los campos de entrada están vacíos
                    cliente = facturas["facturas"][item_index]["cliente"]
                    cancha = facturas["facturas"][item_index]["cancha"]
                    fecha = facturas["facturas"][item_index]["fecha"]
                    hora = facturas["facturas"][item_index]["hora"]
                    horario = facturas["facturas"][item_index]["horario"]
                    iva = self.entrada_iva.get() or facturas["facturas"][item_index]["iva"]
                    precio = facturas["facturas"][item_index]["precio"]

                    
                    facturas["facturas"][item_index] = {
                        "cliente": cliente,
                        "cancha": cancha,
                        "fecha": fecha,
                        "hora": hora,
                        "horario": horario,
                        "iva": iva,
                        "precio": precio
                    
                    }
                
                    with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\FACTURA.json', 'w') as jf:
                        json.dump(facturas, jf, indent=4)

                        messagebox.showinfo("Información", "Factura Actualizada")
                        self.entrada_iva.delete(0, tk.END)

        btnactualizar = tk.Button(self.frame_dinamyc, text="ACTUALIZAR", font= ("Comic Sans MS", 14, "bold"),command= actualizar_Factura)
        btnactualizar.place(x=250, y= 550)



    def limpiar_panel(self,panel):
    # Función para limpiar el contenido del panel
        for widget in panel.winfo_children():
            widget.destroy()