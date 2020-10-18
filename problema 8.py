a=int(input("Primul numar"))
b=int(input("Al doilea numar"))
if (a%2 ==0) and (b%2==0):
    if a<b:
        print(b)
    if a>b:
        print(a)
if (a%2==0) and (b%2!=0):
    print(a)
if (a%2!=0) and (b%2==0):
    print(b)
if (a%2!=0) and (b%2!=0):
    print ("Numerele nu sunt pare")