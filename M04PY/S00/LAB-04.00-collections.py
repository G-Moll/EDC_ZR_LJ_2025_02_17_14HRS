# LISTA o ARREGLOS se estructuran con corchetes: []
# DICCIONARIOS u OBJETOS se estructuran con llaves: {}
# TUPLAS se estructuran con paréntesis: ()

# Lista
notes = [ 10, 5, 7, 8.7, 6.5 ]
print( "LISTA: ", notes )

# Diccionario
student = {
    "name": "Joshua",
    "notes": [ 10, 8, 6, 7, 2.8 ]
}
print( "\nDICCIONARIO: ", student )

# Lista que contiene Diccionarios
groupStudents = [
    { "name": "Joshua", "notes": [ 1 ] },
    { "name": "Martha", "notes": [ 2, 5 , 5 ] },
    { "name": "Pedro", "notes": [ 10, 0 ] }
]
print( "\nLISTA DE DICCIONARIOS: ", groupStudents )

# Diccionario que contiene Listas
groupNotes = {
    "students": [ "Joshua", "Paul", "Mark", "John", "Luke" ],
    "final_notes": [ 10, 9.5, 8.7, 9.3, 8.3 ],
    "approved": [ True, True, True, True, True ]
}
print( "\nDICCIONARIO DE LISTAS: ", groupNotes )

# Lista que contiene distintos tipos de datos
complex_list = [
    10, 20, 80,
    { 
        "a": {},
        "b": [ "c", { "name": "JHS" }, [ True, False ] ]
    }
]
print( "\nLISTA COMPLEJA/COMPUESTA: ", complex_list )

# Diccionario que contiene distintos tipos de datos
complex_dict = {
    "a": 10,
    "b": True,
    "c": [
        [ { "a": [] }, { "b": { "c": [] } } ],
        [ { "x": {} }, { "y": { "z": {} } } ]
    ],
    "d": {}
}
print( "\nDICTIONARIO COMPLEJO/COMPUESTO: ", complex_dict )
