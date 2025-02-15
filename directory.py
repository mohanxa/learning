import os as mos 

print ( mos.getcwd() ) 

mos.chdir('..')

print ( mos.getcwd())

dir = mos.path.join( "/" , "tmp", "python")
print ( dir ) 

if not mos.path.exists(dir ) : 
    mos.mkdir(dir)

    if mos.path.exists(dir ) and not mos.path.exists ( mos.path.join("/","tmp","python3")) :
        mos.rename(dir,mos.path.join("/","tmp","python3"))


else : 
    try:
        mos.rmdir(mos.path.join("/","tmp","python3"))
    except : 
        print ( "Error") 

mydir = mos.path.join("/", "home", "mohan", "Documents","Python")

for root, dir , file in mos.walk(mydir) : 
    #print ( f"root is : {root}")
    #print ( f"dir is : {dir}")
    print ( f"file is : {file} " )

