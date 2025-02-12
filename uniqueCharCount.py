org = "mohansumithadikari"
charCounter : dict = {}

for c in org:
    charCounter[c] = ( charCounter.get(c,0) + 1 )
        
for key, val in charCounter.items():
    print ( '{} - {}'.format(key,val) )

