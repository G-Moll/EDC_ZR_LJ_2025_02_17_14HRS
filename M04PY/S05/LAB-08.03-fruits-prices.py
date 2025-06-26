# 0803 MÉTODOS DE LOS OBJETOS

# Ejercicio 0803 (2 puntos)
#     - Vamos a crear un programa en Python donde vamos a declarar
#         - un diccionario para guardar
#         - los precios de las distintas frutas.

#     # El programa pedirá
#         # el nombre de la fruta
#         # y la cantidad que se ha vendido
#         # y nos mostrará el precio final de la fruta
#             # a partir de los datos guardados en el diccionario.
#         # Si la fruta no existe nos dará un error.
#         # Tras cada consulta
#             # el programa nos preguntará si queremos hacer otra consulta.

fruits_data = {
    "manzana": 40,
    "platano": 20,
    "moras": 30,
    "cereza": 50,
    "kiwi": 40,
    "mango": 25,
    "melon": 20
}
print( fruits_data )

while 1 == 1:

    fruit_choice = input( "Qué fruta quieres? " ) # manzana
    fruit_quantity: int
    
    if fruit_choice not in fruits_data:
        print( "La fruta seleccionada no existe... " )
        continue
    else:
        fruit_quantity = int( input( "Cuanto quieres comprar? " ) )
        fruit_name = fruit_choice
        fruit_price = fruits_data[ fruit_choice ]
        fruit_total = fruit_price * fruit_quantity
        print( f"Fruta { fruit_name }, Precio { fruit_price } Compra Kg{ fruit_quantity }, Total { fruit_total }" )

    new_request = int( input( "Quieres hacer otra compra: (0) Salir, (1) Otra compra: " ) )

    if new_request == 0:
        print( "Gracias por tu compra." )
        break
    elif new_request == 1:
        continue
