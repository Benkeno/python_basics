"""Kapital = 0
Zinsfuss = 0
Tage = 0
Zins = 0
"""
print("Wähle eine Option:")
print("1. Kapital")
print("2. Zinsfuss")
print("3. Tage")
print("4. Zins")
print("9. Ende")

Auswahl = int(input("Deine Auswahl: "))

print("Deine Auswahl war: ", Auswahl)
Case = Auswahl

if Case == 1:
    Zinsfuss = float(input("Zinssatz '%' eingeben: "))
    Tage = int(input("Tage eingeben: "))
    Zins = float(input("Zinsen in € eingeben: "))
    Kapital = float(Zins*100*360) / (Zinsfuss*Tage)
    print("Dafür musst Du der Bank: ", round(Kapital,2), "Euro ausleihen")
elif Case == 2:
    Kapital = float(input("Kapital eingeben in Euro: "))
    Zins = float(input("Zinsen in € eingeben: "))
    Tage = int(input("Tage eingeben: "))
    Zinsfuss = float(Zins*100*360) / (Kapital*Tage)
    print("Zinssatz in '%': ", round(Zinsfuss,2))
elif Case == 3:
    Kapital = float(input("Kapital eingeben in Euro: "))
    Zins = float(input("Zinsen in € eingeben: "))
    Zinsfuss = float(input("Zinssatz '%' eingeben: "))
    Tage = int(Zins*100*360) / (Kapital*Zinsfuss)
    print("Tage: ", round(Tage,0))
elif Case == 4:
    Kapital = float(input("Kapital eingeben in Euro: "))
    Zinsfuss = float(input("Zinssatz '%' eingeben: "))
    Tage = int(input("Tage eingeben: "))
    Zins = float(Kapital*Zinsfuss*Tage)/(100*360)
    print("Zinsen: ", round(Zins,2), "€") 
elif Case == 9:
    print("Tschau !!")

else:
    print("oh nooo !")
