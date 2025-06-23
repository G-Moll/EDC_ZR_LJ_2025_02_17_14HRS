# 0902 PROGRAMACIÓN FUNCIONAL

# Ejercicio 0902 (1.5 puntos)
#     - Obtener el cuadrado de todos los elementos en la lista.

# Lista: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

base_numbers = [ 73, 1, 12 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 37 ]

def squareNumbers( list_numbers ):
    squared_numbers = []
    for n in list_numbers:
        squared_numbers.append( n * n )
    return squared_numbers

print( base_numbers )
print( squareNumbers( base_numbers ) )
