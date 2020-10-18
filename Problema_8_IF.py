n1=int(input("Introduceti numarul"))
n2=int(input("Introduceti numarul"))
if(n1%2==1)and(n2%2==1):
    print("Nu sunt numere pare")
if(n1%2==0)and(n2%2==0):
    if(n1>n2):
        print(n1)
    if(n2>n1):
        print(n2)
if(n1%2==1)and(n2%2==0):
    print(n2)
if(n1%2==0)and(n2%2==1):
    print(n1)  