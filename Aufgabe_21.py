"""
    Bei Eingabe von Zu- oder Abgang in +/- ändert sich der Lagerbestand
    und gibt den neuen Lagerbestand ggf. mit Meldung aus
"""
    
lagerBestand = int(4800)                                            # Variable Initial Lagerbestand
meldeBestand = int(1000)                                            # Variable für Meldebestand
hoechstBestand = int(5000)                                          # Variable für Höchstbestand
mindestBestand = int(500)                                           # Varibale für Mindestbestand
aktuellerBestand = int()                                            # Variable hält aktuellen Stand

print("Aktueller Bestand: ", lagerBestand)                          # Ausgabe Lagerbestand
veraenderung = int(input("Zu oder Abgang +/- in Stück eingeben: ")) # Eingabe der Veränderung

aktuellerBestand = lagerBestand + veraenderung                      # Variable aktueller Bestand aus Vorgaben und Eingaben berechnen
lagerBestand = aktuellerBestand                                     # Lagerbestand nimmt Wert von aktuellem Bestand an

print("Neuer Bestand: ", lagerBestand)                              # Ausgabe neuer Lagerbestand

if lagerBestand <= mindestBestand+(-1):                             # Meldung wenn kleiner Mindestbestand
    print("Mindestbestand unterschritten !!")
if lagerBestand <= meldeBestand and lagerBestand >= mindestBestand: # Meldung wenn gleich/kleiner Meldebestand und gleich/größer Mindestbestand
    print("Meldebestand erreicht bzw. unterschritten !")
if lagerBestand >= hoechstBestand+(1):                              # Meldung wenn größer Höchstbestand
    print("Höchstbestand überschritten !!")
