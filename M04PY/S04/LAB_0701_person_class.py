# 0701 PROGRAMACIÓN ORIENTADA A OBJETOS

# Ejercicio 0701 (2 puntos)
#     - Vamos a crear una clase llamada Persona.
#         - Sus atributos (propiedades) son:
#             - nombre,
#             - edad
#             - y DNI.
#         - Construye los siguientes métodos para la clase:
#             - Un constructor, donde los datos pueden estar vacíos.
#             - Los setters y getters para cada uno de los atributos.
#             - Hay que validar las entradas de datos.
#             - mostrar():
#                 - Muestra los datos de la persona.
#             - esMayorDeEdad():
#                 - Devuelve un valor lógico indicando si es mayor de edad

class Person:
    name: str
    age: int
    rfc: str

    def __init__( self, name, age, rfc ):
        self.name = name
        self.age = age
        self.rfc = rfc
        print( f"Hola soy { self.name } { self.rfc }, tengo { self.age } años" )

personOne = Person( "Joshua", 30, "ABC123" )
personTwo = Person( "Luke", 25, "XYZ456" )
personBis = Person( "John", 18, "NML147" )
