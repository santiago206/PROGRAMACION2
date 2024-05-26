from clases import listar_eliminar
from clases import listaru_eliminaru
from clases import listarn_eliminarn
from clases import listara_eliminara

from clases import Universidad
from clases import Persona
from clases import Notas
from clases import Asignatura



while(True):
    print("\n__MENU PRINCIPAL__")
    print("Elija una de las siguientes opciones: ")
    print("Personas ----> 1")
    print("Universidades ----> 2")
    print("Notas ----> 3")
    print("Asignaturas ----> 4")
    print("Salir ----> 5")

    menu = listar_eliminar(True,True,True,True)
    menu2 = listaru_eliminaru(True,True,True,True)
    menu3 = listarn_eliminarn(True,True,True,True)
    menu4 = listara_eliminara(True,True,True,True)

    numero = int(input("Ingresa un número: "))

    if numero == 1:
        while(True):
            print("\n__SUB MENU__")
            print("Crear persona --> 1")
            print("Listar persona --> 2")
            print("Actualizar persona --> 3")
            print("Eliminar persona --> 4")
            print("Atras --> 5")

            subpersona = int(input("Elije una de las anteriores opciones: "))

            if subpersona == 1:
                menu.crear_persona()
                print("\nlista persona: " + str(Persona))
            elif subpersona == 2:
                menu.listar_persona()
            elif subpersona == 3:
                menu.actualiza_persona()
                print("\nlista Actualizada: " + str(Persona))
            elif subpersona == 4:
                menu.eliminar_persona()
                print("\nlista persona: " + str(Persona))
            elif subpersona == 5:
                break
            else:
                print("\ningrese una opcion valida")
    
    if numero == 2:
        while(True):
            print("\n__SUB MENU__")
            print("Crear universidad --> 1")
            print("Listar universidad --> 2")
            print("Actualizar universidad --> 3")
            print("Eliminar universidad --> 4")
            print("Atras --> 5")

            subuni = int(input("Elije una de las anteriores opciones: "))

            if subuni == 1:
                menu2.crear_universidad()
                print("\nlista Universidad: " + str(Universidad))
            elif subuni == 2:
                menu2.listar_universidad()
            elif subuni == 3:
                menu2.actualiza_univerisidad()
                print("\nlista Actualizada: " + str(Universidad))
            elif subuni == 4:
                menu2.eliminar_universidad()
                print("\nlista Universidad: " + str(Universidad))
            elif subuni == 5:
                break
            else:
                print("\nIngrese una opcion valida")
    
    if numero == 3:
        while(True):
            print("\n__SUB MENU__")
            print("Agegar nota --> 1")
            print("Listar nota --> 2")
            print("Actualizar nota --> 3")
            print("Eliminar nota --> 4")
            print("Atras --> 5")

            subnotas = int(input("Elije una de las anteriores opciones: "))

            if subnotas == 1:
                menu3.crear_notas()
                print("\nLista Notas: " + str(Notas))
            elif subnotas == 2:
                menu3.listar_notas()
                
            elif subnotas == 3:
                menu3.actualiza_notas()
                print("\nLista Notas: " + str(Notas))
            elif subnotas == 4:
                menu3.eliminar_nota()
                print("\nLista Notas: " + str(Notas))
            elif subnotas == 5:
                break
            else:
                print("\ningrese una opcion valida")

    if numero == 4:
        while(True):
            print("\n__SUB MENU__")
            print("Agegar asignatura --> 1")
            print("Listar asignatura --> 2")
            print("Actualizar asignatura --> 3")
            print("Eliminar asignatura --> 4")
            print("Atras --> 5")

            subasignatura = int(input("Elije una de las anteriores opciones: "))

            if subasignatura == 1:
                menu4.crear_asignatura()
                print("\nLista Asignatura: " + str(Asignatura))
            elif subasignatura == 2:
                menu4.listar_asignatura()
            elif subasignatura == 3:
                menu4.actualiza_asignatura()
                print("\nLista Asignatura: " + str(Asignatura))
            elif subasignatura == 4:
                menu4.eliminar_asignatura()
                print("\nLista Asignatura: " + str(Asignatura))
            elif subasignatura == 5:
                break
            else:
                print("\ningrese una opcion valida")

    if numero == 5:
        print("\nProceso Finalizado")
        break
    else:
        print("\nInserte una opcion valida")