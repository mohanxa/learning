
t2 = set ()
t2.add('one')
t2.add('two')
t2.add('three')

print ( type (t2))
print ( t2) 

if 'four' in t2 : 
    t2.remove('four')

try:
    t2.discard('four')
except Exception as error :
    print ( 'error is ',error)

print ( len ( t2))

t2.add('four')
t2.add('four')
print ( len ( t2))

print ( '----------------------------------------------------')

t3 = set ( ['mohan','sumith','adikari'])
print ( t3) 

string : str = 'Mohan Sumith Adikari'
t4 = set (string)
print ( t4)

for x in t4 : 
    print ( x ) 

if ( 'x' not in t4 ) : 
    print ('[x] is not in the list ')

if ( 'u' not in t4 ) : 
    print ( '[u] is not in the list ')
else : 
    print ( '[u] exist in the list ')

itm = t4.pop()
print ( itm)

print ( t4)
x = t4.pop()

for i , val in enumerate(t4) : 
    print ( f'{i}. {val}')


