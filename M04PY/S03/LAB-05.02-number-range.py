# Capturar un número que esté entre el 1 y el 7

user_input = float( input( "Captura un número entre el 1 y el 7" ) )

if user_input < 1 or user_input > 7:
    print( "El número está fuera del rango", user_input )
else:
    print( "Número dentro del rango", user_input )
