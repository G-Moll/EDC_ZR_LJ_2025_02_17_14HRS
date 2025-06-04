# - En una lista se agregarán 10 valores aleatorios
# - para mostrar en pantalla sus cuadrados y sus cubos
import random
list_numbers = []

for x in range( 1, 11 ):
    random_number = random.randint( 1, 20 )
    list_numbers.append( random_number )
    print( "Número Actual: ", random_number )
    print( "Cuadrado: ", random_number * random_number )
    print( "Cubo: ", random_number * random_number * random_number, "\n" )
