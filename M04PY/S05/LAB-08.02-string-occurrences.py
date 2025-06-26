# 0802 MÉTODOS DE LOS OBJETOS

# Ejercicio 0802 (2 puntos)
#     - Escribe un programa
#         - que lea una cadena (input)
#         - y devuelva un diccionario ({})
#             - con la cantidad de apariciones
#             - de cada carácter en la cadena.

# "Hello"
# print( { "H": 1, "e": 1, "l": 2, "o": 1 } )
# Caracter "H", Conteo 1
# Caracter "e", Conteo 1
# Caracter "l", Conteo 2

phrase_chars = {}
input_string = input( "Captura una frase: " )
# input_string = "Lorem ipsum Lorem ipsum ipsum ipsum 123 123 123 @...."

for c in range( len( input_string ) ):
    if not phrase_chars.get( input_string[ c ] ):
        phrase_chars.update( { input_string[ c ]: 1 } )
    else:
        current_key = input_string[ c ]
        updated_value = phrase_chars.get( current_key ) + 1
        phrase_chars[ current_key ] = updated_value

for c in phrase_chars:
    print( f'Caracter { c }, Conteo { phrase_chars[ c ] }'  )

# print( phrase_chars )
