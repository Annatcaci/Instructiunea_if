am=int(input("Bile albe mici "))
rm=int(input("Bile rosii mici "))
vm=int(input("Bile verzi mici "))
ma=int(input("Bile albe mari "))
mr=int(input("Bile rosii mari "))
mv=int(input("Bile verzi mari "))
tm=int(am+rm+vm)
mt=int(ma+mr+mv)
at=int(am+ma)
rt=int(rm+mr)
vt=int(vm+mv)
print("Numarul total de bile= ", tm+mt)
if(tm>mt):
    print("Cele mai numeroase sunt bile mici= ",tm)
elif(mt>mt):
    print("Cele mai numeroase sunt bile mari= ",mt)
else:
    print("Numarul de bile mici si mari sunt egale= ",tm)
if(at>rt)and(at>vt):
    print("Cele mai multe bile sunt de culoarea alba= ", at)
if(rt>at)and(rt>vt):
    print("Cele mai multe bile sunt de culoarea rosie= ", rt)
if(vt>rt)and(vt>at):
    print("Cele mai multe bile sunt de culoarea verde= ", vt)
if(at==rt)and(at>vt):
    print("Cele mai multe bile sunt de culoarea alba si rosii= ", at)
if(vt==rt)and(vt>at):
    print("Cele mai multe bile sunt de culoarea rosii si verde=", rt)
if(at==vt)and(at>rt):
    print("Cele mai multe bile sunt de culoarea alba si verde=", at)
if(at==vt)and(vt==rt):
    print("Toate sunt egale")
