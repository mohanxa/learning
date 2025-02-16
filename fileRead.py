import os as mos

#Method 1
file = open( mos.path.join("/", "home","mohan","Documents","Python","showMeTheMeaning.txt") )
l = file.readlines()
print ( l ) 
file.close()

#Method 2 
file = open( mos.path.join("/", "home","mohan","Documents","Python","showMeTheMeaning.txt") )
while True : 
    l = file.readline()
    if not l : 
        break
    print ( l, end="")
file.close()

#Method 3
with open(mos.path.join("/", "home","mohan","Documents","Python","showMeTheMeaning.txt") ) as f:
    for line in f : 
        print (line.strip())

print ( "EOF")