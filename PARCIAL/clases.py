Persona = []
Universidad = []
Notas = []
Asignatura = []

class menupersona:
    
    def __init__(self,crear):
        self.crear = crear    
    def crear_persona(self):
        nombre = input("Ingrese el nombre de la persona que quiere agregar: ")
        Persona.insert(0,nombre)
        Apellido = input("Ingrese el apellido de la persona que quiere agregar: ")
        Persona.insert(1,Apellido)
        Estatura = input("Ingrese la estatura de la persona que quiere agregar: ")
        Persona.insert(2,Estatura)
        Cedula = input("Ingrese la cedula de la persona que quiere agregar: ")
        Persona.insert(3,Cedula)
        Edad = input("Ingrese la edad de la persona que quiere agregar: ")
        Persona.insert(4,Edad)           
class listar_eliminar (menupersona):
    def __init__(self,crear,listar,eliminar,actualizar):
        super().__init__(crear)
        self.listar = listar
        self.eliminar = eliminar
        self.actualizar = actualizar
        
    def listar_persona(self):
        print("\nlista persona: " + str(Persona))
    def actualiza_persona(self):
        print("\nlista persona: " + str(Persona))
        print("Ingrese la coordenada del elemento y por el cual lo va a cambiar:")
        coordenada = int(input("Cordenada del elemento: "))
        nuevo_dato = input("Ingrese el nuevo elemento: ")

        Persona[coordenada] = nuevo_dato

    def eliminar_persona(self):
        print("\nlista persona: " + str(Persona))
        eliminar = int(input("Ingrese la coordenada del dato que desea eliminar: "))
        Persona.pop(eliminar)
        
#####    
class menuniversidad:

    def __init__(self,crearu):
        self.crearu = crearu    
    def crear_universidad(self):
        nombreu = input("Ingrese el nombre de la universidad que quiere agregar: ")
        Universidad.insert(0,nombreu)
        facultad = input("Ingrese la facultad a la que pertenece: ")
        Universidad.insert(1,facultad)
        carrera = input("Ingrese la carrera que esta estudiando: ")
        Universidad.insert(2,carrera)
        jornada = input("Ingrese su jornada: ")
        Universidad.insert(3,jornada)
        semestre = int(input("Ingrese el numero del semestre que esta cursando: "))
        Universidad.insert(4,semestre)            
class listaru_eliminaru(menuniversidad):
    def __init__(self,crearu,listaru,eliminaru,actualizaru):
        super().__init__(crearu)
        self.listaru = listaru
        self.eliminaru = eliminaru
        self.actualizaru = actualizaru
        
    def listar_universidad(self):
        print("\nlista Universidad: " + str(Universidad))
    def actualiza_univerisidad(self):
        print("\nlista Universidad: " + str(Universidad))
        print("Ingrese la coordenada del elemento y por el cual lo va a cambiar:")
        coordenadaa = int(input("Cordenada del elemento: "))
        nuevo_datoo = input("Ingrese el nuevo elemento: ")

        Universidad[coordenadaa] = nuevo_datoo

    def eliminar_universidad(self):
        print("\nlista Universidad: " + str(Universidad))
        eliminaru = int(input("Ingrese la coordenada del dato que desea eliminar: "))
        Universidad.pop(eliminaru)

##### 
class menunotas:

    def __init__(self,crearn):
        self.crearn = crearn
    
    def crear_notas(self):
        alumno = input("Agrege el nombre del alumno: ")
        Notas.insert(0,alumno)
        n = int(input("Ingrese la primera nota: "))
        Notas.insert(1,n)
        n2 = int(input("Ingrese la segunda nota: "))
        Notas.insert(2,n2)
        n3 = int(input("Ingrese la tercera nota: "))
        Notas.insert(3,n3)
        promedio = ((n + n2 + n3)/3)
        Notas.insert(4,promedio)
        print("Promedio de notas: " + str(promedio))
class listarn_eliminarn(menunotas):
    def __init__(self,crearu,listarn,eliminarn,actualizarn):
        super().__init__(crearu)
        self.listarn = listarn
        self.eliminarn = eliminarn
        self.actualizarn = actualizarn
        
    def listar_notas(self):
        print("\nlista Notas : " + str(Notas))
    def actualiza_notas(self):
        print("\nlista Notas: " + str(Notas))
        print("Ingrese la coordenada del elemento y por el cual lo va a cambiar:")
        coordenadan = int(input("Cordenada del elemento: "))
        nuevo_daton = input("Ingrese el nuevo elemento: ")

        Notas[coordenadan] = nuevo_daton

    def eliminar_nota (self):
        print("\nlista Notas: " + str(Notas))
        eliminarn = int(input("Ingrese la coordenada del dato que desea eliminar: "))
        Notas.pop(eliminarn)

#####
class menuasignatura:

    def __init__(self,creara):
        self.creara = creara

    def crear_asignatura(self):
        profesor = input("Agrege el nombre del profesor: ")
        Asignatura.insert(0,profesor)
        N_asignatura = (input("Ingrese el nombre de la asignatura: "))
        Asignatura.insert(1,N_asignatura)
        salon = int(input("Ingrese el numero del salon: "))
        Asignatura.insert(2,salon)
        piso = int(input("Ingrese el piso donde se ubica el salon: "))
        Asignatura.insert(3,piso)
        numero_estudian= int(input("Ingrese el numero de estudiantes que cursan la asignatura: "))
        Asignatura.insert(4,numero_estudian)
        
class listara_eliminara(menuasignatura):
    def __init__(self,creara,listara,eliminara,actualizara):
        super().__init__(creara)
        self.listara = listara
        self.eliminara = eliminara
        self.actualizara = actualizara
        
    def listar_asignatura(self):
        print("\nlista Asignatura : " + str(Asignatura))
    def actualiza_asignatura(self):
        print("\nlista Asignatura: " + str(Asignatura))
        print("Ingrese la coordenada del elemento y por el cual lo va a cambiar:")
        coordenadas = int(input("Cordenada del elemento: "))
        nuevo_datos = input("Ingrese el nuevo elemento: ")

        Asignatura[coordenadas] = nuevo_datos

    def eliminar_asignatura (self):
        print("\nlista Asignatura: " + str(Asignatura))
        eliminara = int(input("Ingrese la coordenada del dato que desea eliminar: "))
        Asignatura.pop(eliminara)
    
    