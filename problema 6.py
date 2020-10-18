a=int(input("Prima nota="))
b=int(input("A doua nota="))
c=int(input("A treia nota="))
if c>8:
    print(a,b,c)
if c<8:
    if a>b:
        print(a)
    if b<a:
        print(b)
    if a==b:
        print(a)