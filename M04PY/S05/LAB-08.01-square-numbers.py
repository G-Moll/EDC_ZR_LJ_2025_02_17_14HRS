# 0801 MÉTODOS DE LOS OBJETOS

# Ejercicio 0801 (2 puntos)
#     - Escribe un programa Python
#         - que pida un número por teclado
#         - y que cree un diccionario
#             - cuyas claves sean desde el número 1 hasta el número indicado,
#             - y los valores sean los cuadrados de las claves.

squared_number = {}
limit_keys = int( input( "Cuadrados a calcular: " ) )

for n in range( 1, limit_keys + 1 ):
    squared_number[ n ] = n * n
    # squared_number[ n ] = pow( n, 2 )

print( squared_number )
