
org = "mohansumithadikari"
isSorted = False
lst : list = list(org)

while not isSorted:
    isSorted = True
    print ( "".join(lst))
    for x in range ( len(org) - 1 ) : 
        if ( lst[x] > lst[x+1] ) : 
            lst[x], lst[x+1] = lst[x+1],lst[x]
            isSorted = False
org = "".join(lst)
print ( f'Sorted string is {org}')