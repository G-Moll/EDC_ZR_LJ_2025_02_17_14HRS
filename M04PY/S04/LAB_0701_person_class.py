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
    __name: str
    __age: int
    __rfc: str

    def __init__( self, name, age, rfc ):
        self.__name = name
        self.__age = age
        self.__rfc = rfc

    def mostrar( self ):
        return f"Hola soy { self.name } { self.rfc }, tengo { self.age } años"

    def esMayordeEdad( self ):
        return self.age >= 18

    @property
    def name( self ):
        return self.__name
    @name.setter
    def name( self, new_name ):
        self.__name = new_name

    @property
    def age( self ):
        return self.__age
    @age.setter
    def age( self, new_age ):
        self.__age = new_age

    @property
    def rfc( self ):
        return self.__rfc
    @rfc.setter
    def rfc( self, new_rfc  ):
        self.__rfc = new_rfc

personOne = Person( "Joshua", 17, "ABC123" )
print( personOne.mostrar() )
print( personOne.esMayordeEdad() )

# personTwo = Person( "Luke", 25, "XYZ456" )
# personBis = Person( "John", 18, "NML147" )


