# 0604 SENTENCIAS CONDICIONALES

# Ejercicio 0604 (1.5 puntos)
#     - Crea una aplicación que
#     - pida un número
#     - y calcule su factorial
#         # (El factorial de un número es el producto
#         # de todos los enteros entre 1 y el propio número
#         # y se representa por el número seguido de un signo de exclamación.
#         # Por ejemplo 5! = 1x2x3x4x5=120).

factorial_input = int( input( "Captura un número para calcular su factorial: " ) )
factorial_result = 0
current_calculation = 1

if factorial_input > 0:
    for n in range( 1, factorial_input + 1 ):
        current_calculation = current_calculation * n
    print( f"El factorial de { factorial_input } es { current_calculation }" )
else:
    print( "El factorial de cero es 1" )



