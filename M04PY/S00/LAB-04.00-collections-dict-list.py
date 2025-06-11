group = {
    # "a": "Some value",
    # "b": [ 10, True ],
    # "c": {
    #     "x": 1,
    #     "y": [ 20, 30 ],
    #     "z": { "m": False, "l": [ 12, False, "One" ]  }
    # }
}
# print( group[ "c" ][ "z" ][ "l" ][ 2 ] )
# print( group[ "c" ][ "y" ][ 1 ] )
# print( group[ "c" ][ "y" ] )
# print( group[ "c" ][ "x" ] )
# print( group[ "b" ][ 0 ] )
# print( group[ "b" ][ 1 ] )
# print( group )
# print( group[ "a" ] )

students_name = [ "Joshua", "Peter", "Luke", "Mathew", "Paul", "Mark", "John", "Apollo" ]

print( "ADD KEYS( AND VALUES) TO DICTIONARY" )

group[ "Joshua" ] = []
group[ "Peter" ] = []
group[ "Luke" ] = []
group[ "Mathew" ] = []
group[ "Paul" ] = []
group[ "Mark" ] = []
print( "\nOPTION 01: ", group )


group[ students_name[ 0 ] ] = []
group[ students_name[ 1 ] ] = []
group[ students_name[ 2 ] ] = []
group[ students_name[ 3 ] ] = []
group[ students_name[ 4 ] ] = []
group[ students_name[ 5 ] ] = []
print( "\nOPTION 02: ", group )

for student in range( len( students_name ) ):
    group[ students_name[ student ] ] = []
print( "\nOPTION 03: ", group )

for student in students_name:
    group[ student ] = []
print( "\nOPTION 04: ", group )
