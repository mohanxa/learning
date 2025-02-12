line : str = '''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.'''

for n in line : 
    if n.lower() not in ('aeiou'):
        print (n, end='')

nums = range ( 10)

result : int = 0 
for o in nums:
    result += o 
print("")
print ( f'result is {result}')

dct : dict = {'one': 1, 'two': 2, 'three': 3, 'four':4, 'five': 5}
for n in dct:
    print (dct[n])

print ( f'Length of the dictionary is : {len(dct)}')
print ( f'Length of the line is {len(line)}')


prime = True 
for p in range(1,31):
    for q in range (2, p):
        if ( p%q == 0 ):
            print ( f'{p} / {q} = {int(p/q)}')
            prime = False
    if ( prime == True):
        print ( f'{p} is a prime number')
    prime = True 
else : 
    print ('For loop is over ')




