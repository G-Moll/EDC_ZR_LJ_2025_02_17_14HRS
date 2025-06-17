# 0601 SENTENCIAS CONDICIONALES

# Ejercicio 0601 (1.5 puntos)
#     - Realizar un ejemplo de menú,
#         - donde podemos escoger las distintas opciones
#         - hasta que seleccionamos la opción de “Salir”.

menu_description = """
Please choose some (numeric) option:
    1) Café     4) Huevos       7) Pan
    2) Leche    5) Chilaquiles  8) Hot Cakes
    3) Jugo     6) Sandwich     9) Postre

    0) Exit Menu
"""
print( menu_description )

choices = []

while True:
    input_choice = int( input( "Escoge una opción del menú: " ) )
    if input_choice == 0:
        break
    elif input_choice == 1:
        choices.append( "Café" )
    elif input_choice == 2:
        choices.append( "Leche" )
    elif input_choice == 3:
        choices.append( "Jugo" )
    elif input_choice == 4:
        choices.append( "Huevos" )
    elif input_choice == 5:
        choices.append( "Chilaquiles" )
    elif input_choice == 6:
        choices.append( "Sandwich" )
    elif input_choice == 7:
        choices.append( "Pan" )
    elif input_choice == 8:
        choices.append( "Hot Cakes" )
    elif input_choice == 9:
        choices.append( "Postre" )
    else:
        print( "La opción no está en el menú" )

print( "Tus opciones fueron: ", choices )

