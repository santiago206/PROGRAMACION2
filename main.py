from persona import persona

print("MIS DATOS:")

p = persona("santiago","apellido","cedula","correo","telefono")
print(p.imprimirNombre())

p = persona("santiago","jimenez ferrer","cedula","correo","telefono")
print(p.imprimirApellido())

p = persona("santiago","jimenez ferrer","1142914126","correo","telefono")
print(p.imprimirCedula())

p = persona("santiago","jimenez ferrer","1142914126","sant@gmail.com","telefono")
print(p.imprimirCorreo())

p = persona("santiago","jimenez ferrer","1142914126","sant@gmail.com","311440094")
print(p.imprimirTelefono())

