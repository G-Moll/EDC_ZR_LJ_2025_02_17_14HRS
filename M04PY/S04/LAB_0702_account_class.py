# 0702 PROGRAMACIÓN ORIENTADA A OBJETOS

# Ejercicio 0702 (2 puntos)
#     - Crea una clase llamada Cuenta
#         - que tendrá los siguientes atributos:
#             - titular, que es una persona (Person)
#             - y cantidad (puede tener decimales).
#                 - El titular será obligatorio
#                 - y la cantidad es opcional.
#         - Construye los siguientes métodos para la clase:
#             - Un constructor (__init__()),
#                 - donde los datos pueden estar vacíos.
#             - Los setters y getters para cada uno de los atributos.
#                 - El atributo no se puede modificar directamente,
#                 - sólo ingresando o retirando dinero.
#             - mostrar(): showSavings()
#                 - Muestra los datos de la cuenta.
#             - ingresar(cantidad): deposit()
#                 - se ingresa una cantidad a la cuenta,
#                 - si la cantidad introducida es negativa, no se hará nada.
#             - retirar(cantidad): withdraw()
#                 - se retira una cantidad a la cuenta.
#                 - La cuenta puede estar en números rojos.

from LAB_0701_person_class import Person

class Account:
    __account_holder: Person
    __account_balance: float
    __account_opening: float

    def __init__( self, account_holder, account_opening = 0 ):
        self.__account_holder = account_holder
        self.__account_opening = account_opening
        self.__account_balance = self.__account_opening

    def showSavings( self ):
        print( f"El balance es ${ self.account_balance }" )

    def deposit( self, ammount ):
        current_balance = self.account_balance
        self.account_balance = current_balance + ammount

    def withdraw( self, ammount ):
        current_balance = self.account_balance
        self.account_balance = current_balance - ammount


    @property
    def account_holder( self ):
        return self.__account_holder
    
    @property
    def account_balance( self ):
        return self.__account_balance
    @account_balance.setter
    def account_balance( self, new_balance ):
        self.__account_balance = new_balance
    
    @property
    def account_opening( self ):
        return self.__account_opening

joshua = Person( "Joshua", 30, "ABC113377" )
account = Account( joshua, 500 )

account.showSavings()
account.deposit( 200 )
account.showSavings()
account.withdraw( 50 )
account.showSavings()

# print( account.account_holder.showInfo() )
# print( account.account_balance )
