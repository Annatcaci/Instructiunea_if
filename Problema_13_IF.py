n=int(input("Numarmarul lui Ionel"))
if (n%4==1):
    print("Va primi tricou alb")
elif(n%4==3):
    print("Va primi tricou albastru")
elif (n%4==2):
    print("Va primi tricou rosu")
elif(n%4==0):
    print("Va primi tricou negru")
else:
    print("Nu a participat")