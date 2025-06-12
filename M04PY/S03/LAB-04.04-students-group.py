students_group = {}
students_quantity = int( input( "Número de alumnos: " ) )

for student in range( students_quantity ):
    current_student_name = input( "Estudiante " + str( student + 1 ) + ": "  )
    current_student_notes = []

    while True:
        current_note = int( input( "Captura una calificación: " ) )
        if current_note > 10:
            current_note = 10
        elif current_note < 0:
            break
        current_student_notes.append( current_note )
    students_group[ current_student_name ] = current_student_notes

print( "INFORMACIÓN DEL GRUPO" )
for current_student in students_group:
    current_notes = students_group[ current_student ]
    current_quantity_notes = len( current_notes )
    message = f"\tNombre: { current_student } \n\tNúm Notas: { current_quantity_notes } \n\tPromedio { sum( current_notes ) / current_quantity_notes } \n\tCalificaciones: { current_notes }\n"
    print( message )

print( students_group )
