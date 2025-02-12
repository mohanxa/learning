org = "mohansumithadikari"
lst = []

for i in range ( len(org) ) :
    if ( org[i] not in lst ):
        lst.append(org[i])

print (f"result is {"".join(lst)}")
