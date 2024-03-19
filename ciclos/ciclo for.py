
volar  = {
    "Aerolínea" : "volaris" ,
    "Vuelo" : "AV789" ,
    "Origen" : "CTG" ,
    "Destino" : "MDE" ,
    "Tipo_Maleta" : [ 'Cabina' , 'Mano' , 'Bodega' ]
}


print( "Valores del diccionario: " )
for  key , value in volar.items ():
   print ( f" { key } : { value } " )


print ( " \n Valores del tipo de maleta: " )
for  tipo_maleta in volar [ "Tipo_Maleta" ]:
    print ( tipo_maleta )
