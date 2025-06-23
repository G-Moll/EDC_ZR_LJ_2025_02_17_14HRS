# 0904 PROGRAMACIÓN FUNCIONAL

# Ejercicio 0904 (1.5 puntos)
#     - Obtener la suma de todos los elementos en la lista.
list_numbers_one = [ 4, 6, 7, 90, 15, 20, 7, 46 ]
list_numbers_two = [ 40, 60, 7, 90, 15 ]
list_numbers_bis = [ 7, 80, 3 ]

def sumList( list_numbers ):
    list_sum = 0
    for n in list_numbers:
        list_sum += n
    # return list_sum
    return { "sum": list_sum }

result_one = sumList( list_numbers_one )
result_two = sumList( list_numbers_two )
result_bis = sumList( list_numbers_bis )

print( result_one, result_two, result_bis[ "sum" ] )

