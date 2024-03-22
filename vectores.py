
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

print(Datos_personales)

# paso 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']

# paso 7
it_companies.insert(3,'Garena')
print(it_companies)

# paso 8
does_exist = 'Google' in it_companies
print(does_exist)

# paso 9
it_companies.sort()
print(it_companies)

# paso 10
revertir_lista = it_companies[::-1]
print(revertir_lista)

#paso 11
it_companies.remove('Facebook')
print(it_companies)

# paso 12
it_companies.clear()
print(it_companies)