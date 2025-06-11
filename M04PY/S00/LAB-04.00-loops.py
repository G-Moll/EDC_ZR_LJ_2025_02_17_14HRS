# for x in range(10):
#     pass

while True:
    note = int( input( "Captura una calificación: " ) )
    if note > 10:
        note = 10
    elif note < 0:
        break
    print( "Captura: ", note )
