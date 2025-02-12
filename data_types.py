
mynum : int = 10
mystr : str = "Mohan Adikari"
mydecimal : float = 100.40
mybool : bool = True 

#print ( "My name is ", mystr, " and age is ",mynum ," and my decimal is ", mydecimal) 

mynames : list = ["mohan", "gayan", "nuwan", "Thevidu"]
#print ( mynames[0])

mynames2 : tuple = [12,43,55,66,44]
#print ( mynames2[0])

mynames3 : set = {23,22,22,345}
#print ( mynames3[2])

data : dict = {'name':'Mohan', 'age':23}
print ( data["name"]);
print ( data.get("name"))

complex_data : dict = { 'one' : {'name':'Mohan','age':44} , 'two': {'name':'gayan','age':43}}
print ( complex_data['two']['age'])

s = range(1,10,2)

for var in s : 
    print ( f"{var:03}")

 


