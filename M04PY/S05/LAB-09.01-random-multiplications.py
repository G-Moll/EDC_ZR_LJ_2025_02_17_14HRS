# 0901 PROGRAMACIÓN FUNCIONAL

# Ejercicio 0901 (1.5 puntos)
#     - Realice un programa que pregunte aleatoriamente una multiplicación.
#         - El programa debe indicar
#             - si la respuesta ha sido correcta o no
#             - (en caso que la respuesta sea incorrecta el programa debe indicar cuál es la correcta).

#     # El programa preguntará 10 multiplicaciones,
#     # y al finalizar mostrará el número de aciertos.

import random

def randomMultiplication():
    attempt = {}
    attempt[ "num_one" ] = random.randint( 1, 10 )
    attempt[ "num_two" ] = random.randint( 1, 10 )
    attempt[ "mult_numbers" ] = attempt[ "num_one" ] * attempt[ "num_two" ]
    return attempt

def promptUser():
    attempt_results = { "right": 0, "wrong": 0, "matches": [] }
    num = 0
    while num < 10:
        current_multiplication = randomMultiplication()
        num_one = current_multiplication[ "num_one" ]
        num_two = current_multiplication[ "num_two" ]
        mult_numbers = current_multiplication[ "mult_numbers" ]

        user_answer = int( input( f"Resultado de multiplicar { num_one } x { num_two }: " ) )

        if user_answer != mult_numbers:
            attempt_results[ "wrong" ] += 1 
        else:
            attempt_results[ "right" ] += 1

        attempt_results[ "matches" ].append( { "pc": mult_numbers, "user": user_answer, "matched": mult_numbers == user_answer } )
        num += 1

    return attempt_results

def showResults( data_results ):
    answers = "\n"
    for n in data_results[ 'matches' ]:
        # current_value = ""
        # if n[ 'matched' ] == True:
        #     current_value = "Sí"
        #     n[ 'matched' ] = "Sí"
        # else:
        #     current_value = "No"
        #     n[ 'matched' ] = "No"

        # answers += f"PC: { n[ 'pc' ] }, Usuario: { n[ 'user' ] }, Coincide: { current_value }\n"
        
        answers += f"\tPC: { n[ 'pc' ] }, Usuario: { n[ 'user' ] }, Coincide: { 'Sí' if n[ 'matched' ] else 'No' }\n"

    results = f"""
Aciertos: { data_results[ 'right' ] }
Desaciertos:  { data_results[ 'wrong' ] }
Preguntas:  { answers }
    """
    return results


# user_results = promptUser()
# data_results = showResults( user_results )
# print( data_results )

print( showResults( promptUser() ) )



# Operador Ternario Python
# "Sí" if 1 == 1 else "No"
# "Sí" if 2 == 1 else "No"

# if 1 == 1:
#     "Sí" 
# else:
#     "No"

# Operador Ternario Otros lenguajes
# True ? "Sí" : "No"
# False ? "Sí" : "No"
