n1=int(input("Introduceti numerele elevilor"))
n2=int(input())
n3=int(input())
p1=int(input("Introduceti punctajul elevilor"))
p2=int(input())
p3=int(input())
if (p1>p2)and(p1>p3):
    print("Cel mai mare punctaj are juctorul", n1)
elif (p2>p3)and(p2>p1):
    print("Cel mai mare punctaj are juctorul", n2)
elif (p2==p3)and(p2>p1):
    print("Cel mai mare punctaj au juctorul", n2, n3)
elif (p3>p1)and(p3>p2):
    print("Cel mai mare punctaj are juctorul", n3)
elif (p1==p3)and(p1>p2):
    print("Cel mai mare punctaj au juctorul", n1, n3)
elif (p1==p2)and(p2>p3):
    print("Cel mai mare punctaj au juctorul", n2)
else:
    print("La toti egal")