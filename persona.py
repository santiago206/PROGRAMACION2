class persona:
    def __init__(self,nombre,apellido,cedula,correo,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.correo = correo
        self.telefono = telefono

    def imprimirNombre(self):
        return f'Nombre: {self.nombre}'
    def imprimirApellido(self):
        return f'Apellidos: {self.apellido}'
    def imprimirCedula(self):
        return f'Cedula: {self.cedula}'
    def imprimirCorreo(self):
        return f'Correo: {self.correo}'
    def imprimirTelefono(self):
        return f'Telefono: {self.telefono}'
    
    
p = ("santiago","jimenez ferrer","1142914126","sant@gmail.com","311440094")







