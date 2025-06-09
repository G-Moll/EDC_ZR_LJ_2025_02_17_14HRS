group = {}
students_name = [ "Joshua", "Peter", "Luke", "Mathew", "Paul", "Mark" ]

for student in range( len( students_name ) ):
    group[ students_name[ student ] ] = []
print( group )

for student in students_name:
    group[ student ] = []
print( group )
