import tkinter as tk
import util.generic as utl
import os
import json
from tkinter import ttk
from tkinter import messagebox
import random
from datetime import datetime, timedelta

class Barberia(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Barberia")
        self.resizable(False, False)
  
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        self.geometry(f"{ancho_pantalla}x{alto_pantalla}")

        self.imagen = utl.leer_imagen("\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\imagenes\\barber logo.png", (200, 200))
        
        frame1 = tk.Frame(self,bg="grey")
        frame1.place(x= 0 ,y=0,width=1500,height=1000)

        archivo_json = "\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\CORTES.json"

        with open(archivo_json, "r") as archivo:
            cortes = json.load(archivo)

            nombres_cortes = cortes[0]
            imagenes_cortes = cortes[1]

        archivo_json = "\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\VENTAS.json"

        with open(archivo_json, "r") as archivo:
            ventas = json.load(archivo)

            precios = ventas[0]

        self.frame_logo = tk.Label(frame1, bd=0,relief=tk.SOLID,image=self.imagen)
        self.frame_logo.place(x= 50, y= 50)

        imagen1 = imagenes_cortes[0]
        nombre1 = nombres_cortes[0]
        precios1 = precios[0]

        self.imagen1 = utl.leer_imagen(imagen1, (200, 200))

        self.corte1 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="grey",image=self.imagen1)
        self.corte1.place(x= 300, y= 80, width= 200, height= 200)

        self.nombre1 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(nombre1))
        self.nombre1.place(x= 300, y= 300, width= 200, height= 30)

        self.precio1 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(precios1))
        self.precio1.place(x= 300, y= 330, width= 200, height= 30)

        imagen2 = imagenes_cortes[1]
        nombre2 = nombres_cortes[1]
        precios2 = precios[1]

        self.imagen2 = utl.leer_imagen(imagen2, (200, 200))

        self.corte2 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="grey",image=self.imagen2)
        self.corte2.place(x= 550 , y= 80, width= 200, height= 200)

        self.nombre2 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(nombre2))
        self.nombre2.place(x= 550, y= 300, width= 200, height= 30)

        self.precio2 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(precios2))
        self.precio2.place(x= 550, y= 330, width= 200, height= 30)

        imagen3 = imagenes_cortes[2]
        nombre3 = nombres_cortes[2]
        precios3 = precios[2]

        self.imagen3 = utl.leer_imagen(imagen3, (200, 200))

        self.corte3 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="grey",image=self.imagen3)
        self.corte3.place(x= 800, y= 80, width= 200, height= 200)

        self.nombre3 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(nombre3))
        self.nombre3.place(x= 800, y= 300, width= 200, height= 30)

        self.precio3 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(precios3))
        self.precio3.place(x= 800, y= 330, width= 200, height= 30)

        imagen4 = imagenes_cortes[3]
        nombre4 = nombres_cortes[3]
        precios4 = precios[3]

        self.imagen4 = utl.leer_imagen(imagen4, (200, 200))

        self.corte4 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="grey",image=self.imagen4)
        self.corte4.place(x= 1050 , y= 80, width= 200, height= 200)

        self.nombre4 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(nombre4))
        self.nombre4.place(x= 1050, y= 300, width= 200, height= 30)

        self.precio4 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(precios4))
        self.precio4.place(x= 1050, y= 330, width= 200, height= 30)

        imagen5 = imagenes_cortes[4]
        nombre5 = nombres_cortes[4]
        precios5 = precios[4]

        self.imagen5 = utl.leer_imagen(imagen5, (200, 200))

        self.corte5 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="grey",image=self.imagen5)
        self.corte5.place(x= 300, y= 380, width= 200, height= 200)

        self.nombre5 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(nombre5))
        self.nombre5.place(x= 300, y= 600, width= 200, height= 30)

        self.precio5 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(precios5))
        self.precio5.place(x= 300, y= 630, width= 200, height= 30)

        imagen6 = imagenes_cortes[5]
        nombre6 = nombres_cortes[5]
        precios6 = precios[5]

        self.imagen6 = utl.leer_imagen(imagen6, (200, 200))

        self.corte6 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="grey",image=self.imagen6)
        self.corte6.place(x= 550 , y= 380, width= 200, height= 200)

        self.nombre6 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(nombre6))
        self.nombre6.place(x= 550, y= 600, width= 200, height= 30)

        self.precio6 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(precios6))
        self.precio6.place(x= 550, y= 630, width= 200, height= 30)

        imagen7 = imagenes_cortes[6]
        nombre7 = nombres_cortes[6]
        precios7 = precios[6]

        self.imagen7 = utl.leer_imagen(imagen7, (200, 200))

        self.corte7 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="grey",image=self.imagen7)
        self.corte7.place(x= 800, y= 380, width= 200, height= 200)

        self.nombre7 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(nombre7))
        self.nombre7.place(x= 800, y= 600, width= 200, height= 30)

        self.precio7 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(precios7))
        self.precio7.place(x= 800, y= 630, width= 200, height= 30)


        imagen8 = imagenes_cortes[7]
        nombre8 = nombres_cortes[7]
        precios8 = precios[7]

        self.imagen8 = utl.leer_imagen(imagen8, (200, 200))

        self.corte8 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="grey",image=self.imagen8)
        self.corte8.place(x= 1050 , y= 380, width= 200, height= 200)

        self.nombre8 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(nombre8))
        self.nombre8.place(x= 1050, y= 600, width= 200, height= 30)

        self.precio8 = tk.Label(frame1, bd=0,relief=tk.SOLID,background="white",text= str(precios8))
        self.precio8.place(x= 1050, y= 630, width= 200, height= 30)

        def hacer_reservacion():

            ventana = tk.Tk()
            ventana.geometry("400x300")
            ventana.title("Reservacion")

            elegir = tk.Label(ventana,text= "Elije el corte: ")
            elegir.place(x= 50, y= 100)

            nombre = tk.Label(ventana,text= "Nombre: ")
            nombre.place(x= 50, y= 50)

            nombre_entrada = tk.Entry(ventana)
            nombre_entrada.place(x= 200, y= 50)

            opciones = [str(nombres_cortes[0]),str(nombres_cortes[1]),
                        str(nombres_cortes[2]),str(nombres_cortes[3]),
                        str(nombres_cortes[4]),str(nombres_cortes[5]),
                        str(nombres_cortes[6]),str(nombres_cortes[7])]
            combo = ttk.Combobox(ventana, values=opciones)
            combo.place(x=200,y=100)


            etiqueta = tk.Label(ventana, text="")
            etiqueta.pack(pady=5)


            def seleccionar_opcion():
               
             archivo_json = "\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\RESERVAS.json"

             with open(archivo_json, "r") as archivo:
              reservas = json.load(archivo)

             def fecha_random(lista_fechas):
    
              fechas = [datetime.strptime(fecha, '%Y-%m-%d') for fecha in lista_fechas]
    
              fecha_min = min(fechas)
              fecha_max = max(fechas)
    
              diferencia = fecha_max - fecha_min
    
              dias_aleatorios = random.randint(0, diferencia.days)
    
 
              fecha_aleatoria = fecha_min + timedelta(days=dias_aleatorios)
    
              return fecha_aleatoria


             fechas = reservas[0]

             fecha_aleatoria = fecha_random(fechas)

             def hora_random(lista_horas):
    
               horas = [datetime.strptime(hora, '%H:%M') for hora in lista_horas]
    
               hora_min = min(horas).replace(second=0)
               hora_max = max(horas).replace(second=0)
    
               diferencia = hora_max - hora_min

               minutos_aleatorios = random.randint(0, int(diferencia.total_seconds() / 60))
     
               hora_aleatoria = hora_min + timedelta(minutes=minutos_aleatorios)
    
               return hora_aleatoria

             horas = reservas[1]

             hora_aleatoria = hora_random(horas)

             nombre_persona = nombre_entrada.get()
             seleccion = combo.get()

             archivo_jso = "\\Users\\USUARIO\\Desktop\\PARCIAL 3\\LoginApp\\data\\VENTAS.json"

             with open(archivo_jso, "r") as archivo:
               ventas = json.load(archivo)

               total_ventas = ventas[1]

             precio = ""

             if seleccion == nombres_cortes[0]:
                precio = precios1

                total_ventas.append(precio)
                with open(archivo_jso, "w") as archivo:
                  json.dump(ventas, archivo, indent=2)

             elif seleccion == str(nombres_cortes[1]):
                precio = precios2
                total_ventas.append(precio)
                with open(archivo_jso, "w") as archivo:
                  json.dump(ventas, archivo, indent=2)

             elif seleccion == str(nombres_cortes[2]):
                precio = precios3
                total_ventas.append(precio)
                with open(archivo_jso, "w") as archivo:
                  json.dump(ventas, archivo, indent=2)

             elif seleccion == str(nombres_cortes[3]):
                precio = precios4
                total_ventas.append(precio)
                with open(archivo_jso, "w") as archivo:
                  json.dump(ventas, archivo, indent=2)

             elif seleccion == str(nombres_cortes[4]):
                precio = precios5
                total_ventas.append(precio)
                with open(archivo_jso, "w") as archivo:
                  json.dump(ventas, archivo, indent=2)

             elif seleccion == str(nombres_cortes[5]):
                precio = precios6
                total_ventas.append(precio)
                with open(archivo_jso, "w") as archivo:
                  json.dump(ventas, archivo, indent=2)

             elif seleccion == str(nombres_cortes[6]):
                precio = precios7
                total_ventas.append(precio)
                with open(archivo_jso, "w") as archivo:
                  json.dump(ventas, archivo, indent=2)
             else:
                precio = precios8
                total_ventas.append(precio)
                with open(archivo_jso, "w") as archivo:
                  json.dump(ventas, archivo, indent=2)

             messagebox.showinfo("Factura", "Nombre:  " + (nombre_persona) + "\n" + "Corte:  " + seleccion + "\n" + "Precio:  " + str(precio) + "$" + "\n" + "Fecha: " + str(fecha_aleatoria.strftime('%Y-%m-%d')) + "\n" + "Hora: " + hora_aleatoria.strftime('%H:%M') )

             lista_de_reservas = reservas[2]
             lista_de_reservas.append("Nombre:  " + (nombre_persona) + "  Corte:  " + seleccion  + "   Precio:  " + str(precio) + "$" +  "  Fecha: " + str(fecha_aleatoria.strftime('%Y-%m-%d')) + "  Hora: " + hora_aleatoria.strftime('%H:%M'))

             with open(archivo_json, "w") as archivo:
                json.dump(reservas, archivo, indent=2)

             ventana.destroy()

             
            boton = tk.Button(ventana, text="Reservar",command= seleccionar_opcion)
            boton.place(x= 200 ,y= 150)

            
            ventana.mainloop()

        self.reservar = tk.Button(frame1, text= "RESERVAR",bg="black",fg="white" ,font="Helvetica 13",command= hacer_reservacion)
        self.reservar.place(x= 70,y= 350)

