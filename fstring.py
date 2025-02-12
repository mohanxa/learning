first_name : str = 'Mohan'
last_name : str  = 'Adikari'

sentence : str = 'My name is {} {}'. format ( first_name,last_name)
print ( sentence)

sentence2 : str = f'My name is {first_name} {last_name}'
print ( sentence2)

# Using dictionary
dct : dict = {'int_val': 3004, 'str_val' : 'Sring value ', 'compex_val' : {'x': 'value_one', 'y': 'value_two'} }
mystr : str = f"{dct['int_val']} and complex value {dct['compex_val']['y']}"
print ( mystr)

dct2 : dict = {
    'name' : 'Mohan Adikari',
    'address' : 'Mawaramandiya',
    'other' : { 
        'job' : 'Programmer',
        'salary' : '10400040',
        'date_joined' : '1-Jan-2020'
    }
}

fstr : str = f"{dct2['other']['job'].upper()} is the job of employee"
print ( fstr ) 

#calculation withing fstring 
fstr2 : str = f"Multiplication of 50 and 30 is {50 * 30}"
print ( fstr2)