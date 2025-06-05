# Diccionario
student = {
    "name": "Joshua",
    "notes": [ 10, 8, 6, 7, 2.8]
}
print( student )

# Lista que contiene Diccionarios
group = [
    { "name": "Joshua", "notes": [ 1 ]  },
    { "name": "Martha", "notes": [ 2, 5 , 5 ]  },
    { "name": "Pedro", "notes": [ 10, 0 ]  }
]
print( group )

# Lista que contiene distintos tipos de datos
some_list = [
    10, 20, 80,
    { 
        "a":{},
        "b":[ "c", { "name": "JHS" }, [ True, False ] ]
    }
]
print( some_list )

# Diccionario que contiene distintos tipos de datos
dict_one = {
    "a": 10,
    "b": True,
    "c": [
        [ { "a":[] }, { "b":{ "c":[] } } ]
        [ { "x":{} }, { "y":{ "z":{} } } ]
    ],
    "d": {}
}
print( dict_one )

