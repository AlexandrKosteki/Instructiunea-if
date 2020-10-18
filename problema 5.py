zn=int(input("ziua nasterii"))
ln=int(input("luna nasterii"))
an=int(input("anul nasterii"))
zc=int(input("ziua curenta"))
lc=int(input("luna curenta"))
an=int(input("anul curent"))
if lc>ln:
    print(ac-an)
if (lc==ln) and (zn>zc):
    print(ac-an)
if lc<ln:
    print((ac-an)-1)
if (lc==ln) and (zn<zc):
    print((ac-an)-1)