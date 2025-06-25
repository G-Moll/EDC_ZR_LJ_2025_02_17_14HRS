def cuadrado( num ):
    return num * num

# def puedeVotar():
#     return user_age >= 18

def puedeVotar( edad ):
    return edad >= 18

abc = 18
puede_votar = puedeVotar( abc )
print( puede_votar )

# print( puedeVotar( 16 ) )
# print( puedeVotar( 21 ) )
