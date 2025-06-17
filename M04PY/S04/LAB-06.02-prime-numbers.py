# 0602 SENTENCIAS CONDICIONALES

# Ejercicio 0602 (1.5 puntos)
#     - Mostrar en pantalla los N primero número primos.
#     - Se pide por teclado la cantidad de números primos que queremos mostrar.

from data.primes import prime_numbers

input_choice = int( input( "Cuántos números primos quieres mostrar? " ) )

if input_choice > len( prime_numbers ):
    print( "No hay tantos números para mostrar..." )
elif input_choice == 0:
    print( "No quieres mostrar números primos..." )
elif input_choice > 0 and input_choice <= len( prime_numbers ):
    print( prime_numbers[ : input_choice ] )
    # print( prime_numbers[ 0 : input_choice ] )
