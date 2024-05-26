import tkinter as tk
from tkinter import ttk

def obtener_hora():
    hora = spinbox_horas.get()
    minutos = spinbox_minutos.get()
    print(f"La hora seleccionada es: {hora}:{minutos}")


root = tk.Tk()
root.title("Seleccionar Hora")
frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Crear Spinbox para las horas (1 a 12 para formato de 12 horas)
spinbox_horas = ttk.Spinbox(frame, from_=1, to=12, width=5, wrap=True)
spinbox_horas.grid(row=0, column=0, padx=5, pady=5)
# Crear Spinbox para los minutos (0 a 59)
spinbox_minutos = ttk.Spinbox(frame, from_=0, to=59, width=5, wrap=True, format="%02.0f")
spinbox_minutos.grid(row=0, column=1, padx=5, pady=5)

spinbox_horas.bind("<<ComboboxSelected>>", obtener_hora)
spinbox_minutos.bind("<<ComboboxSelected>>", obtener_hora)


# Ejecutar la aplicación
root.mainloop()