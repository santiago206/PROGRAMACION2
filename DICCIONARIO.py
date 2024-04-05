
#paso 1
perro = {}

#paso2
perro ['Nombre'] = 'francisco'
perro['Color'] = 'blanco'
perro['Raza'] = 'bulldog'
perro['Patas'] = '4'
perro['edad'] ='2 años'
print("Datos de la lista perro: " + str(perro))

#paso 3
Estudiante = {}
Estudiante ['nombre'] = 'Santiago'
Estudiante['Apellido'] = 'Jimenez Ferrer'
Estudiante['Sexo'] = 'Masculino'
Estudiante['Edad']= '18'
Estudiante ['Estado civil'] = 'Soltero'
Estudiante ['habilidades']= 'jugar futbol'
Estudiante ['país'] = 'Colombia'
Estudiante ['Ciudad'] = 'Cartagena'
Estudiante ['Dirección'] = '13 de junio'


#paso 4
print("numero de elementos de la lista estudiante: " + str(len(Estudiante)))

#paso 5
print("habilidades: " + str(Estudiante['habilidades']))

#paso 6
Estudiante['habilidades'] = "velocidad","resistencia"

#paso 7
claves = Estudiante.keys()
print("Claves: \n" + str(claves))

#paso 8
valores = Estudiante.values()
print("Valores: \n" + str(valores))

#paso 9
print("Tuplas: \n" + str(Estudiante.items()))

#paso 10
Estudiante.pop('nombre')
print("lista sin el elemento nombre: \n" + str(Estudiante))

#paso 11
del Estudiante


