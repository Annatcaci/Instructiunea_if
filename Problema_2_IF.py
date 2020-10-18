l1=int(input("Prima latura"))
l2=int(input("A doua latura"))
l3=int(input("A treia latura"))
if (l1<l2+l3)and(l2<l3+l1)and(l3<l2+l1):
    print("da")
else:
    print("Nu")