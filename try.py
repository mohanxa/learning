choises = {1: 'Very Good', 2:'Modarate', 3: 'Poor'}

try : 
    val = int ( input ('Enter value to search' ) )
    choise = choises[val]
except ValueError as err1 : 
    print ( f"Your value not in the list {err1}")
except KeyError as err2: 
    print ( f"We are having error {err2}")
else : 
    print (f"You selected {choise}")
finally:
    print ("Operation completed")