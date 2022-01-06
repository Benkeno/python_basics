 #


#---------- Eingabe -----------------------------

tag = int(input("Tag eingeben: "))              #  Eingabe String als Integer
monat = int(input("Monat eingeben: "))
jahr = int(input("Jahr eingeben: "))


    
jahr1 = int(jahr / 100)                             # Teile Jahr durch 100 (Ganzzahliger Rest weil Int)
jahr2 = int(jahr % 100)                             # Divisionsrest von 100 (Modulo)                                  

h1 = int(((monat * 13) - 1) % 5)                    # Monat * 13 - 1 Divisionsrest 5 berechnen
h2 = int((jahr2 / 4))                               # Jahr2 / 4 berechnen
h3 = int(jahr1 / 4)                                 # Jahr1 / 4 berechnen

b = int(h1 + h2 + h3)                               # Summe h1 h2 h3 berechnen
f = int(((b + jahr2 + tag) - (jahr1 *2)) % 7)       # Divisonsrest 

wochentag = str()                                   # Variable Wochentag (leer) für Buchstaben deklarieren

#----------- Verarbeitung ----------------------------

if monat < 3:                                       # wenn Monat kleiner 3
     monat += 10                                  # erhöhe Monat um 10
     jahr -= 1                                    # und Verringern Jahr um 1
else: monat -= 2
                                                    # sonst Monat um 2 verringern
if f == 0:                                          # wenn int  f 0 (if)
    wochentag = "Sonntag"                           # wird string Sonntag
elif f == 1:                                        # sonst wenn int f (elif = else... if)
        wochentag = "Montag"                        # wird string Montag    
elif f == 2:                                        #.....
        wochentag = "Dienstag"
elif f == 3:
        wochentag = "Mittwoch"
elif f == 4:
        wochentag = "Donnestag"
elif f == 5:
        wochentag = "Freitag"
elif f == 6:
        wochentag = "Samstag"

else:                                               # sonst (else)
    (print("Hahahaha !!"))

#--------------------   Ausgabe  ------------------------------

print("Der", tag, monat, jahr," war ein ", wochentag)           # Ausgabe als String
