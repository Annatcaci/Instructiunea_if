n1=int(input("Introduceti numarul"))
n2=int(input("Introduceti numarul"))
n3=int(input("Introduceti numarul"))
if(n1>0)and(n2>0)and(n3>0):
    if(n2>n3):
        print(n2)
    if(n3>n2):
        print(n3)
elif(n1<0)or(n2<0)or(n3<0):
    print(n1+n2)
else:
    print("Error")