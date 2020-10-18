n1=int(input("Introdu nr elevului"))
n2=int(input("Introdu nr la al dolea elev"))
n3=int(input("Introdu nr al trilea elev"))
p1=int(input("Introdu punctjul 1="))
p2=int(input("Introdu punctajul 2="))
p3=int(input("Introdu punctajul 3="))
if (p1>p2) and (p1>p3):
    print(n1)
if (p2>p1) and (p2>p3):
    print(n2)
if (p3>p1) and (p3>p2):
    print(n3)
if (p1==p2) and (p1>p3) and (p2>p3):
    print(n1,n2)
if (p2==p3) and (p2>p1) and (p3>p1):
    print(n2,n3)
if (p1==p3) and (p1>p2) and (p3>p2):
    print(n1,n3)