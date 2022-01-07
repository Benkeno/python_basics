AnfangsTempKaffee = int(input("Gib die Kaffeetemperatur ein: "))
Zimmertemperatur = 21
AbnahmeFaktor = 10
Abnahme = 0
NeueTempKaffee = 0
Minute = 0
Differenz = AnfangsTempKaffee - Zimmertemperatur
print("Die Zimmertemperatur beträgt: ", Zimmertemperatur,"° Grad")
print("Die Differenz beträgt: ", Differenz, "° Grad")

if AnfangsTempKaffee < 0 or AnfangsTempKaffee > 100:
    print("Ungültige Eingabe !!")
#else:
    #print("juhu")

while Differenz > 0.5:
    Minute = Minute + 1
    Differenz = Differenz - (Differenz / 100 * AbnahmeFaktor)
    Abnahme = AnfangsTempKaffee - Differenz - Zimmertemperatur
    NeueTempKaffee = AnfangsTempKaffee - Abnahme

    
    print("Minute:", Minute, "; Temperaturabnahme:", round(Abnahme,2), "°; Differenz:",round(Differenz,2), "°; Neue Temperatur:", round(NeueTempKaffee,2),"° Grad")
    if Differenz < 0.5:
        print("Kaffee kalt !!")