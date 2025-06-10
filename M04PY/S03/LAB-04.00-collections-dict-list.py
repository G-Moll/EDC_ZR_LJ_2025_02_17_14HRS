group = {}
students_name = [ "Joshua", "Peter", "Luke", "Mathew", "Paul", "Mark" ]

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
