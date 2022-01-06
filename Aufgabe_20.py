"""
Kundenrabatt je nach Geschäftsdauer und Vorjahresumsatz gestaffelt
"""


UmsatzAktuell = float (input("Zu zahlender Betrag: "))
LetzterUmsatz = int (input("Vorjahresumsatz eingeben: "))
Dauer = int (input("Dauer der Geschäftsverbindung eingeben: "))
Rabatt = int
if LetzterUmsatz > 100000 and Dauer >= 5:   # wenn Vorjahresumsatz gleich/grösser und Dauer gleich/grösser als
    Rabatt  = 30                            
if LetzterUmsatz > 100000 and Dauer <= 4:   # wenn Vorjahresumsatz gleich/grösser und Dauer gleich/kleiner als
    Rabatt = 28
if LetzterUmsatz < 999999 and Dauer >= 2:   # wenn Vorjahresumsatz gleich/kleiner und Dauer gleich/grösser als
    Rabatt  = 24
if LetzterUmsatz > 999999 and Dauer <= 1:   # wenn Vorjahresumsatz gleich/kleiner und Dauer gleich/kleiner als
    Rabatt = 22
print("Bei",UmsatzAktuell, "Warenwert", "erhalten Sie ",Rabatt, "% Rabatt", "Das macht nun: ",round(UmsatzAktuell-(Rabatt/100)*UmsatzAktuell,2), "Euro")
