# - Capturar 5 valores de cadenas por medio de la consola
# - Agregar esos valores a una lista
# - Agregar esos mismos valores a una segunda lista, pero en orden inverso
first_list = []
reverse_list = []

while len( first_list ) < 5:
    user_input = input( "Captura una palabra: " )
    first_list.append( user_input )
    reverse_list.insert( 0, user_input )

print( first_list )
print( reverse_list )



