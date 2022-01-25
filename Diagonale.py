from math import sqrt

print("Was möchtest Du berechnen ?")
print("1. Diagonale eines Rechtecks berechnen")
print("2. Diagonalen eines Quaders berechnen")

Auswahl = int(input("Deine Auswahl: "))

if Auswahl == 1:
    a = float(input("Länge der Seite A eingeben: "))
    b = float(input("Länge der Seite B eingeben: "))

    diagonale = sqrt(a**2+b**2)

    print(round(diagonale,2))

elif Auswahl == 2:
    a = float(input("Länge der Seite A eingeben: "))
    b = float(input("Länge der Seite B eingeben: "))   
    c = float(input("Länge der Seite C eingeben: "))

    diagonale = sqrt(a**2+b**2)
    rmdiagonale = sqrt(diagonale**2 + c**2) 

    print("Diagonale A-B: ",round(diagonale,2), "Raumdiagonale: ", round(rmdiagonale,2))

else: 
    print("Naa !!")

