class persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def imprimir(self):
        return f'mi nombre es {self.nombre} {self.apellido}'
    
P = persona("santiago","jimenez")
print(P.imprimir())
