Anfangsbestand = 3500
Endbestand = 2000
UmsatzEinstandsPreis = 375000
Durchschnittsumsatz = 0
DurchschnittlicheLagerdauer = 0
DurchschnittlicherLagerbestand = (Anfangsbestand /2) 
Umsatzgeschwindigkeit = UmsatzEinstandsPreis / DurchschnittlicherLagerbestand

print("Wähle eine Option:")
print("1. Durchschnittlicher Lagerbestand")
print("2. Umsatzgeschindigkeit")
print("3. Durchschnittliche Lagerdauer")
print("9. Programm abbrechen")

Wahl = int(input())
print("Ihre Wahl", Wahl)

if Wahl == 1:
    print(round(DurchschnittlicherLagerbestand,1))
elif Wahl == 2:
    print("Umsatzgeschwindikeit", round(UmsatzEinstandsPreis / DurchschnittlicherLagerbestand,1))
elif Wahl == 3:
    print("Lagerdauer", round(360 / Umsatzgeschwindigkeit,1))
elif Wahl == 9:
    print("Tschüss")
else:
    print("Falsche Eingabe")


 