zc=int(input("Introduceti ziua curenta"))
lc=int(input("Introduceti luna curenta"))
ac=int(input("Introduceti anul curenta"))
zn=int(input("Introduceti ziua nasterii"))
ln=int(input("Introduceti luan nasterii"))
an=int(input("Introduceti anul nasterii"))
if(lc<ln):
    print((ac-an)-1)
else:
    print(ac-an)