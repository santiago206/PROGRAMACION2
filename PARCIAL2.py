
Persona = ["santiago","johana"]
Universidad = ["Tecnar","UDC"]
Notas = [2,5]
Asignatura = ["castellano","matematicas"]

class menupersona:

    def __init__(self,crear,listar,eliminar):
        self.crear = crear
        self.listar = listar
        self.eliminar = eliminar
    
    def crear_persona(self):
        nombre = input("ingrese el nombre de la persona que quiere agregar: ")
        Persona.insert(0,nombre)
    def listar_persona(self):
        print(Persona)
    def eliminar_persona(self):
        eliminar = input("ingrese el nombre de la persona que desea eliminar: ")
        Persona.remove(eliminar)
    
class menuniversidad:

    def __init__(self,crearu,listaru,eliminaru):
        self.crearu = crearu
        self.listaru = listaru
        self.eliminaru = eliminaru
    
    def crear_universidad(self):
        nombreu = input("ingrese el nombre de la universidad que quiere agregar: ")
        Universidad.insert(0,nombreu)
    def listar_univeridad(self):
        print(Universidad)
    def eliminar_universidad(self):
        eliminar2 = input("ingrese el nombre de la universidad que desea eliminar: ")
        Universidad.remove(eliminar2)

class menunotas:

    def __init__(self,crearn,listarn,eliminarn):
        self.crearn = crearn
        self.listarn = listarn
        self.eliminarn = eliminarn
    
    def crear_notas(self):
        nombren = input("ingrese la nota que quiere agregar: ")
        Notas.insert(0,nombren)
    def listar_notas(self):
        print(Notas)
    def eliminar_notas(self):
        eliminar3= input("ingrese la nota que desea eliminar: ")
        Notas.remove(eliminar3)

class menuasignatura:

    def __init__(self,creara,listara,eliminara):
        self.creara = creara
        self.listara = listara
        self.eliminara = eliminara
    
    def crear_asignatura(self):
        Nasignatura = input("ingrese el nombre de la asignatura que quiere agregar: ")
        Asignatura.insert(0,Nasignatura)
    def listar_asignatura(self):
        print(Asignatura)
    def eliminar_asignatura(self):
        eliminar4 = input("ingrese el nombre de la asignatura que desea eliminar: ")
        Asignatura.remove(eliminar4)

while(True):
    print("\n__MENU PRINCIPAL__")
    print("Elija una de las siguientes opciones: ")
    print("Personas ----> 1")
    print("Universidades ----> 2")
    print("Notas ----> 3")
    print("Asignaturas ----> 4")
    print("Salir ----> 5")

    menu = menupersona(True, True, True)
    menu2 = menuniversidad(True,True,True)
    menu3 = menunotas(True,True,True)
    menu4 = menuasignatura(True,True,True)

    numero = int(input("Ingresa un número: "))

    if numero == 1:
        while(True):
            print("\n__SUB MENU__")
            print("Crear persona --> 1")
            print("Listar persona --> 2")
            print("Eliminar persona --> 3")
            print("Atras --> 4")

            subpersona = int(input("elije una de las anteriores opciones: "))

            if subpersona == 1:
                menu.crear_persona()
                print(Persona)
            elif subpersona == 2:
                menu.listar_persona()
                print(Persona)
            elif subpersona == 3:
                menu.eliminar_persona()
                print(Persona)
            elif subpersona == 4:
                break
            else:
                print("ingrese una opcion valida")
    
    if numero == 2:
        while(True):
            print("__SUB MENU__")
            print("Crear universidad --> 1")
            print("Listar universidad --> 2")
            print("Eliminar universidad --> 3")
            print("Atras --> 4")

            subuni = int(input("elije una de las anteriores opciones: "))

            if subuni == 1:
                menu2.crear_universidad()
                print(Universidad)
            elif subuni == 2:
                menu2.listar_univeridad()
                print(Universidad)
            elif subuni == 3:
                menu2.eliminar_universidad()
                print(Universidad)
            elif subuni == 4:
                break
            else:
                print("ingrese una opcion valida")
    
    if numero == 3:
        while(True):
            print("__SUB MENU__")
            print("Agegar nota --> 1")
            print("Listar nota --> 2")
            print("Eliminar nota --> 3")
            print("Atras --> 4")

            subnotas = int(input("elije una de las anteriores opciones: "))

            if subnotas == 1:
                menu3.crear_notas()
                print(Notas)
            elif subnotas == 2:
                menu3.listar_notas()
                print(Notas)
            elif subnotas == 3:
                menu3.eliminar_notas()
                print(Notas)
            elif subnotas == 4:
                break
            else:
                print("ingrese una opcion valida")

    if numero == 4:
        while(True):
            print("__SUB MENU__")
            print("Agegar asignatura --> 1")
            print("Listar asignatura --> 2")
            print("Eliminar asignatura --> 3")
            print("Atras --> 4")

            subasignatura = int(input("elije una de las anteriores opciones: "))

            if subasignatura == 1:
                menu4.crear_asignatura()
                print(Asignatura)
            elif subasignatura == 2:
                menu4.listar_asignatura()
                print(Asignatura)
            elif subasignatura == 3:
                menu4.eliminar_asignatura()
                print(Asignatura)
            elif subasignatura == 4:
                break
            else:
                print("ingrese una opcion valida")

    if numero == 5:
        print("Proceso Finalizado")
        break
    else:
        print("inserte una opcion valida")