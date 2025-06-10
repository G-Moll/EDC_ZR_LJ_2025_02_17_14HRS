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
    current_student_name = input( "Nombre del alumno: " )
    students_group[ current_student_name ] = []

print( students_group )




