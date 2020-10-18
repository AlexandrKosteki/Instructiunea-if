a=int(input("Prima latura="))
b=int(input("A doua latura="))
c=int(input("A treia latura="))
if (a<b+c) and (b<a+c) and (c<a+b):
    print("Da")
else:
    print("nu")
