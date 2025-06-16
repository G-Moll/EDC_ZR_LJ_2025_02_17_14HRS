# Tupla de los meses del año
# El usuario captura un valor enter el 1 y el 12
# Mostrar el mes que corresponde a ese número capturado
# Validar que el rango esté dentro de esos números (1 y 12)
# Que cuando el usuario necesite terminar la app, capture un 0
months = ( "Ene", "Feb", "Mar", "Abr","May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic" )
instructions = """
OPCIÓN A:   Escribe 0 para Salir del programa
OPCIÓN B:   Escribe un número entre 1 y 12 para escoger un mes
    1: Ene \t 2: Feb \t 3: Mar
    4: Abr \t 5: May \t 6: Jun
    7: Jul \t 8: Ago \t 9: Sep
    10: Oct \t 11: Nov \t 12: Dic
"""
print( instructions )

while True:
    user_option = int( input( "Captura un número" ) )

    if user_option == 0:
        print( "Hasta luego" )
        break
    elif user_option < 1 or user_option > len( months ):
        print( "Tu opción está fuera del rango" )
    else:
        print( "Tu opción es: ", months[ user_option - 1 ] )
