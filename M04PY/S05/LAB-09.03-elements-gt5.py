# 0903 PROGRAMACIÓN FUNCIONAL

# Ejercicio 0903 (1.5 puntos)
#     - Obtener la cantidad de elementos mayores a 5 en la tupla.
#     # tupla = (5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3)

tupla_data = ( 5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3 )
number_edge = 5

def getUpperNumbers( tuple_numbers ):
    chosen_numbers = []
    for n in tuple_numbers:
        if n > number_edge:
            chosen_numbers.append( n )
    result = {
        "total": len( chosen_numbers ),
        "numbers": chosen_numbers
    }
    return result

result_one = getUpperNumbers( ( 6, 3, 4, 2, 7, 8, 73 ) )
result_two = getUpperNumbers( tupla_data )
print( result_one )
print( result_two )
