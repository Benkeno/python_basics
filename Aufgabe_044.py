Rechnungsbetrag = float (input("Zu zahlender Betrag: "))
LetzterUmsatz = int (input("Vorjahresumsatz eingeben: "))
#Dauer = int (input("Dauer der Geschäftsverbindung eingeben: "))
Rabatt = int

if LetzterUmsatz <= 500 and Rechnungsbetrag <= 100:   # wenn Vorjahresumsatz gleich/grösser und Dauer gleich/grösser als
    Rabatt  = 0                            
if LetzterUmsatz >= 500 and Rechnungsbetrag <= 100:   # wenn Vorjahresumsatz gleich/grösser und Dauer gleich/grösser als
    Rabatt  = 2                            

if LetzterUmsatz <= 1000 and Rechnungsbetrag >= 100:   # wenn Vorjahresumsatz gleich/grösser und Dauer gleich/grösser als
    Rabatt  = 3                            
if LetzterUmsatz >= 1000 and Rechnungsbetrag >= 1000:   # wenn Vorjahresumsatz gleich/grösser und Dauer gleich/kleiner als
    Rabatt = 4
if LetzterUmsatz <= 2500 and Rechnungsbetrag >= 1000:   # wenn Vorjahresumsatz gleich/kleiner und Dauer gleich/grösser als
    Rabatt  = 5
if LetzterUmsatz >= 2500 and Rechnungsbetrag <= 5000:   # wenn Vorjahresumsatz gleich/kleiner und Dauer gleich/kleiner als
    Rabatt = 6
print("Bei",Rechnungsbetrag, "Warenwert", "erhalten Sie ",Rabatt, "% Rabatt", "Das macht nun: ",round(Rechnungsbetrag-(Rabatt/100)*Rechnungsbetrag,2), "Euro")
