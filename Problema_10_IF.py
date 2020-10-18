ng=int(input("Numarul de gaini "))
nb=int(input("Numarul de boabe "))
bp=int(nb//ng)
bc=int(nb%ng)
if(bp==bc):
    print("egalitate= ", bp)
if(bp>bc):
    print("Gaini= ", bp)
else:
    print("Curcan= ",bc)