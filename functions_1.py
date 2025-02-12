def greeting(iname  ):
    print (f"Good morning {iname}")
    return 

greeting("Mohan")

var = 10 

def printRefId ( prm) : 
    print( f'[inside func]Id of the parameter {id(prm)}')
    prm += 1 
    print( f'[inside func]Id of the parameter after increment {id(prm)}')

print( f'Id before calling function {id(var)}')
printRefId(var)
print( f'value after calling function is {var}')
print( f'Id after calling function {id(var)}')

def printInfo ( name, age = 22 ): 
    print ( f'Name is : {name}')
    print ( f'Age is {age}')

printInfo(age=32, name="Mohan")

printInfo(name="Gayan")

printInfo("Kamal")

def printVariables ( arg1 , *arg2 ) : 
    print ( f'Argument 1 is {arg1}')
    for x in arg2 : 
        print ( f'Values of Arg2 {x}')

printVariables(12,13,14,15,"Mohan","Gayan")

def fcn(nums, numericlist = []):
   numericlist.append(nums + 1)
   print(numericlist) 
    
# function calls
fcn(66)
fcn(68)
fcn(70)

def Stringapprnd ( val , appVal="" ): 
    appVal += val 
    print ( appVal)

Stringapprnd("Mohan")
Stringapprnd("Gayan")
Stringapprnd("Kamal")

def dctArguments ( **val ) : 
    for s in val :
        print ( val[s] ) 
    
    if "name" in val :
        print (f'Customer is {val["name"]}')


dctArguments(name="Mohan" , age="23", Address="Mawanella")

def addr(**kwargs):
   for k,v in kwargs.items():
      print ("{}:{}".format(k,v))

print ("pass two keyword args")
addr(Name="John", City="Mumbai")
print ("pass four keyword args")

# pass four keyword args
addr(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001")

dct : dict = {'id': 'I00001', 'name': 'Mohan Adikari', 'age':32,'Address': 'Mawanella'}
for x,y in dct .items():
    print ( '{} - {}'.format(x,y))

    
