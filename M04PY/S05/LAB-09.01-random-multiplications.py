# 0901 PROGRAMACIÓN FUNCIONAL

# Ejercicio 0901 (1.5 puntos)
#     - Realice un programa que pregunte aleatoriamente una multiplicación.
#         - El programa debe indicar
#             - si la respuesta ha sido correcta o no
#             - (en caso que la respuesta sea incorrecta el programa debe indicar cuál es la correcta).

#     # El programa preguntará 10 multiplicaciones,
#     # y al finalizar mostrará el número de aciertos.

import random

user_results = { "right": 0, "wrong": 0, "matches": [] }

def randomMultiplication():
    attempt = {}
    attempt[ "num_one" ] = random.randint( 1, 10 )
    attempt[ "num_two" ] = random.randint( 1, 10 )
    attempt[ "mult_numbers" ] = attempt[ "num_one" ] * attempt[ "num_two" ]
    return attempt

def promptUser():
    num = 0
    while num < 3:
        current_multiplication = randomMultiplication()
        num_one = current_multiplication[ "num_one" ]
        num_two = current_multiplication[ "num_two" ]
        mult_numbers = current_multiplication[ "mult_numbers" ]

        user_answer = int( input( f"Resultado de multiplicar { num_one } x { num_two }: " ) )

        if user_answer != mult_numbers:
            user_results[ "wrong" ] += 1 
        else:
            user_results[ "right" ] += 1 
        user_results[ "matches" ].append( { "pc": mult_numbers, "user": user_answer, "matched": mult_numbers == user_answer } )
        num += 1

    return "Preguntas completadas"


def showResults():
    print( user_results )

promptUser()
showResults()
