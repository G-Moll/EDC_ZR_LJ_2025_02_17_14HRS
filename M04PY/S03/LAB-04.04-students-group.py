# - Guardar nombres de alumnos de un grupo
#     - Guardar notas que ha tenido cada alumno
#     - Cada alumno puede tener distinta cantidad de notas
#     - La información debe ser guardadada en un Diccionario
#         - Las llaves(/claves/keys) son los nombres de los alumnos
#         - los valores serán las notas de cada alumno
#     - El programa debe mostrar
#         - La lista de alumnos
#         - el promedio de cada uno de ellos

#     - Considerar cuando ya existe un alumno con cierto nombre dentro del grupo

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

print( students_group )
