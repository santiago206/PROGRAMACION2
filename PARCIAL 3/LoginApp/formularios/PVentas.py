import tkinter as tk
import json
from tkinter import messagebox, ttk
import util.generic as utl
class PVentas(tk.Tk):
    def __init__(self, name="", username="", email=""):
        self.name = name
        self.username = username
        self.email = email
        super().__init__()
        self.title("Panel Ventas")
        self.resizable(False, False)
        
        self.ancho_pantalla = self.winfo_screenwidth()
        self.alto_pantalla = self.winfo_screenheight() 

        self.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}")
        
        menubar = tk.Menu(self)  

        menuclientes = tk.Menu(menubar, tearoff=0)
        menuclientes.add_command(label="Ver reservas", command=self.confirmar_reserva)  
        menuclientes.add_command(label="Listar Ventas", command=self.listar_ventas)  
        menubar.add_cascade(label="Ventas", menu=menuclientes)


        self.config(menu=menubar)

        # frame user info

        self.frame_user_info = tk.Frame(self, bd=0,relief=tk.SOLID, width=200,background= "gray25")
        self.frame_user_info.pack(side=tk.LEFT, padx=4, pady=5,fill="y")

        texto=tk.Label(self.frame_user_info, text="       PANEL VENTAS       ",font= ("Comic Sans MS", 20, "bold") ,fg= "White" ,bg="gray25")
        texto.pack(padx=20,pady=4)

        self.usrimg = utl.leer_imagen("\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\imagenes\\logo vendedor.png", (200, 200))
        self.imgusr=tk.Label(self.frame_user_info,image= self.usrimg , background= "gray25",width= 250,height=200)
        self.imgusr.pack(padx=30,pady=4)
        texto1=tk.Label(self.frame_user_info, text=self.name, font= ("Comic Sans MS", 14),fg= "White" ,bg="gray25")
        texto1.pack(padx=40,pady=4)
        texto1=tk.Label(self.frame_user_info, text=self.email, font= ("Comic Sans MS", 14),fg= "White" ,bg="gray25")
        texto1.pack(padx=50,pady=4)
        
        #frame_data
        
        self.frame_data = tk.Frame(self, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_data.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)
        
        #frame_dinamyc
        self.frame_dinamyc = tk.Frame(self.frame_data, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}",background="white")
        self.frame_dinamyc.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)
        self.venimg = utl.leer_imagen("\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\imagenes\\logo ventas.png", (400, 400))
        self.venini=tk.Label(self.frame_dinamyc,image= self.venimg , background= "white",width= 400, height= 400)
        self.venini.pack(pady= 100)

    def confirmar_reserva(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="LISTADO DE RESERVAS", font=('Times',16),fg="#9fa8da")
        labelform.place(x=70, y=70)
        
        with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\FACTURA.json', 'r') as jf:
            facturas = json.load(jf)

        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="LISTADO DE RESERVAS", font= ("Comic Sans MS", 16 ,"bold") ,bg = "white")
        labelform.place(x=20, y=40)
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("Cancha", "Fecha", "Hora","Horario"))
        self.tablausuarios.heading("#0", text="Cliente")
        self.tablausuarios.heading("Cancha", text="Cancha")
        self.tablausuarios.heading("Fecha", text="Fecha")
        self.tablausuarios.heading("Hora", text="Hora")
        self.tablausuarios.heading("Horario", text="Horario")
        with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\FACTURA.json', "r", encoding='utf-8') as file:
                facturas = json.load(file)
                for fact in facturas["facturas"]:
                    self.tablausuarios.insert("", "end", text=f'{fact["cliente"]}',values=(f'{fact["cancha"]}',f'{fact["fecha"]}',f'{fact["hora"]}',f'{fact["horario"]}'))
        self.tablausuarios.place(x=20, y= 90 ,width= 930)
        
        
        self.tablausuarios.bind("<<TreeviewSelect>>",self.mostrar_reservas)


    def mostrar_reservas(self,event):

        labelcliente = tk.Label(self.frame_dinamyc,bg="white" ,font= ("Comic Sans MS", 12))
        labelcliente.place(x=20,y= 330)

        labelcancha = tk.Label(self.frame_dinamyc,bg="white",font= ("Comic Sans MS", 12))
        labelcancha.place(x=20,y= 360)

        labelfecha = tk.Label(self.frame_dinamyc,bg="white" ,font= ("Comic Sans MS", 12))
        labelfecha.place(x=20,y= 390)

        labelhora = tk.Label(self.frame_dinamyc,bg="white" ,font= ("Comic Sans MS", 12))
        labelhora.place(x=20,y= 420)
        
        labelhorario = tk.Label(self.frame_dinamyc,bg="white" ,font= ("Comic Sans MS", 12))
        labelhorario.place(x=20,y= 450)

        labeltotal = tk.Label(self.frame_dinamyc,bg="white" ,font= ("Comic Sans MS", 12))
        labeltotal.place(x=20,y= 490)
        

        
        selected_items = self.tablausuarios.selection()

        if not selected_items:
            
            labelcliente.config(text="")
            labelcancha.config(text="")
            labelfecha.config(text="")
            labelhora.config(text="")
            labelhorario.config(text="")
        
        else:
            try:
                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\FACTURA.json', 'r') as jf:
                        facturas = json.load(jf)
                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CANCHAS.json', 'r') as jf:
                        canchas = json.load(jf)
            except FileNotFoundError:
                    facturas = {"factura": []}
            
            for item in selected_items:
                    item_index = self.tablausuarios.index(item)

                    cliente = facturas["facturas"][item_index]["cliente"]
                    cancha = facturas["facturas"][item_index]["cancha"]
                    fecha = facturas["facturas"][item_index]["fecha"]
                    hora = facturas["facturas"][item_index]["hora"]
                    horario = facturas["facturas"][item_index]["horario"]
                    precio = facturas["facturas"][item_index]["precio"]
                    iva = facturas["facturas"][item_index]["iva"]
                    image = canchas["canchas"][item_index]["Imagen"]
        
                    labelcliente.config(text= "Cliente  : " + str(cliente))
                    labelcancha.config(text= "Cancha  :" + str(cancha))
                    labelfecha.config(text= "Fecha  :" + str(fecha))
                    labelhora.config(text= "Hora  :" + str(hora))
                    labelhorario.config(text= "Horario  :" + str(horario))

                    iva = float(iva)
                    precio_con_iva = int(precio) * (1 +  (iva / 100))

                    self.imagen = str(image)
                    self.ima = utl.leer_imagen(str(self.imagen), (250, 180))
                    labelimagen = tk.Label(self.frame_dinamyc ,bg="blue" ,image=self.ima,font= ("Comic Sans MS", 12))
                    labelimagen.place(x=250,y= 330, height= 180 , width= 250)

                    labeltotal.config(text= "Total a Pagar  :" + str(precio_con_iva))

        def guardar_venta():
            
            with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\VENTAS.json', 'r') as jf:
                    ventas = json.load(jf)

            selected_items = self.tablausuarios.selection()

            if not selected_items:
                    messagebox.showwarning("Advertencia", "Seleccione una reserva")
                    return

            try:
                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\FACTURA.json', 'r') as jf:
                        facturas = json.load(jf)
            except FileNotFoundError:
                    facturas = {"reservas": []}
            
            for item in selected_items:
                    item_index = self.tablausuarios.index(item)

                    cliente = facturas["facturas"][item_index]["cliente"]
                    precio = facturas["facturas"][item_index]["precio"]
                    iva = facturas["facturas"][item_index]["iva"]

                    iva = float(iva)
                    precio_con_iva = int(precio) * (1 +  (iva / 100))
                    
                    ventas["ventas"].append( {
                        "cliente": cliente,
                        "total de la venta" : precio_con_iva
                    })
                
                    with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\VENTAS.json', 'w') as jf:
                        json.dump(ventas, jf, indent=4)

                        messagebox.showinfo("Información", "Venta Registrada")
                        cancelar_reserva()
        
        def cancelar_reserva():
            try:
                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\FACTURA.json', 'r') as jf:
                    facturas = json.load(jf)

                with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\RESERVAS.json', 'r') as jf:
                    reservass = json.load(jf)
            except FileNotFoundError:
                facturas = {"reservas": []}
                reservass = {"reservas": []}
            
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
                del facturas["facturas"][item_index]
                del reservass["reservas"][item_index]

            # Actualizar el archivo JSON
            with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\FACTURA.json', 'w') as jf:
                json.dump(facturas, jf, indent=4)

            with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\RESERVAS.json', 'w') as jf:
                json.dump(reservass, jf, indent=4)



        btneliminar = tk.Button(self.frame_dinamyc, text="CANCELAR RESERVA", font=('Times',14),command=cancelar_reserva)
        btneliminar.place(x=250, y= 550)
        
        btnguardar = tk.Button(self.frame_dinamyc, text="CONFIRMAR RESERVA", font=('Times',14),command=guardar_venta)
        btnguardar.place(x=20, y= 550)
                        
    def listar_ventas(self):

        with open('C:\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\VENTAS.json', 'r') as jf:
            ventas = json.load(jf)

        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="LISTADO DE VENTAS", font= ("Comic Sans MS", 16 ,"bold") ,bg = "white")
        labelform.place(x=20, y=40)
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("Cliente","total de la venta"))
        self.tablausuarios.heading("#0", text="Cliente")

        with open('\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\VENTAS.json', "r", encoding='utf-8') as file:
                ventas = json.load(file)
                for ven in ventas["ventas"]:
                    self.tablausuarios.insert("", "end", text=f'{ven["cliente"]}',values=(f'{ven["total de la venta"]}'))
        self.tablausuarios.place(x=20, y= 90 ,width= 600)


    def limpiar_panel(self,panel):
    # Función para limpiar el contenido del panel
        for widget in panel.winfo_children():
            widget.destroy()