a=int(input("Primul numar"))
b=int(input("Al doilea numar"))
c=int(input("Al treilea numar"))
if (a>0) and (b>0) and (c>0):
    if b>c:
        print(b)
    if b<c:
        print(c)
if (a<0) and (b<0) and (c<0):
    print(a+b)