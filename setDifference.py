s1 = {'java','c++','c#','python','c','rpg'}
s2 = {'c++','python', 'cobol','javacript','acembly'}

s3 = set.difference(s2,s1)

print ( s3)

s4 = s1 - s2

print ( s4)


print ( "-----------------------------------------------")

s5 = set.symmetric_difference(s1,s2)
print ( s5)

s6 = s1 ^ s2 
print ( s6 )