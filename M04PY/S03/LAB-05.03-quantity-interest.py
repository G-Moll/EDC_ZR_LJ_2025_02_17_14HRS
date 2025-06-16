print( """""" )

quantity = float( input( "Captura el capital: " ) )
interest = float( input( "Captura el interés: " ) ) / 100
total = 0

if interest >= 0.3:
    total = quantity + ( quantity * interest )
    print( "El total es : ", total )
else:
    print( "El total es : ", quantity )


