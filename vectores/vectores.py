
## paso 1
lista_vacia= []

## paso 2
jugadores= ['messi', 'neymar', 'suarez','iniesta', 'alves','puyol','mascherano']

## paso 3
print('Numero de jugadores:',len(jugadores))
print(len(lista_vacia))

# paso 4     
primer_jugador = jugadores[0]
print("Primer jugador: " + primer_jugador)
medio_jugador = jugadores[len(jugadores)//2]
print("Jugador del medio: " + medio_jugador)
ultimo_jugador = jugadores[-1]
print("Ultimo jugador: " + ultimo_jugador)

# paso 5
Datos_personales = []
Datos_personales.append("santiago jimenez")
Datos_personales.append(18)
Datos_personales.append(1.77)
Datos_personales.append("soltero")
Datos_personales.append("13 de junio")


# paso 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']

# paso 7
it_companies.insert(3,'Garena')
print('lista con la nueva empresa: ' + str(it_companies))


# Paso 8
does_exist = 'Google' in it_companies
print('¿El elemento existe en la lista?: ' + str(does_exist))

# Paso 9
it_companies.sort()
print('Lista organizada: ' + str(it_companies))

# Paso 10
revertir_lista = it_companies[::-1]
print('Lista invertida: ' + str(revertir_lista))


#paso 11
it_companies.pop(0)
print('lista con elemento eliminado: ' + str(it_companies))

del it_companies [4]
print('lista con elemento eliminado: ' + str(it_companies))

# paso 12
it_companies.clear()
print('elementos eliminados: ' + str(it_companies))