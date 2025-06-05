# - Leer 5 datos por consola, que representan las notas de un alumno
# - Mostrar todas notas
# - Mostrar el máximo
# - Mostrar el mímino
# - Mostrar el promedio

student_notes = []
while len( student_notes ) < 5:
    current_note = float( input( "Captura una nota: " ) )
    if current_note > 10:
        current_note = 10
    elif current_note < 0:
        current_note = 0
    student_notes.append( current_note )

print( "NOTAS DEL ESTUDIANTE" )
print( "Todas las notas: ", student_notes )
print( "Máximo: ", max( student_notes ) )
print( "Mínimo: ", min( student_notes ) )
print( "Promedio: ", sum( student_notes ) / len( student_notes ) )
