x1=int(input("Numarul petlelor de pe floare"))
ip="Ma ubeste un pic"
im="Ma iubeste mult"
icp="Ma iubeste cu pasiune"
iln="Ma iubeste la nebunie"
idl="Ma iubeste de loc"
if x1>0:
    if(x1-(x1//6)*6)==0:
        print(ip)
    elif(x1-(x1//6)*6)==1:
        print(im)
    elif(x1-(x1//6)*6)==2:
        print(icp)
    elif(x1-(x1//6)*6)==3:
        print(iln)
    elif(x1-(x1//6)*6)==4:
        print(idl)
else:
    print("Eroare")

