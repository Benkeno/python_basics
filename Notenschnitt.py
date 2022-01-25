# Dieses Programm rechnet nach Eingabe von 3 Noten die fehlende 4. Note zum Wunschdurchschnitt


note1 = float(input("Erste Prüfungsnote Eingeben: "))
note2 = float(input("Zweite Prüfungsnote Eingeben: "))
note3 = float(input("Dritte Prüfungsnote Eingeben: "))
wunsch = float(input("Wunschdurchschnitt eingeben: "))

note4 = wunsch * 4 - note1 - note2 - note3

if(note4 >= 1.0 or note4 <= 6.0):
    print("Du benötigst eine", round(note4,1), "um einen Schnitt von", round(wunsch,1), "zu erhalten")
else:
    print("hmm")