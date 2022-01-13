try:
    print('Das ist ein Programm zur Durchschnittstemperatur')
    print('Bitte 3 Werte eingeben')

    temp1 = float(input("1. Wert: "))
    temp2 = float(input("2. Wert: "))
    temp3 = float(input("3. Wert: "))
    durchschnitt = float(temp1 + temp2 + temp3) / 3

    print("Es wurde folgendes eingegeben: {0} °C, {1} °C, {2} °C".format(temp1, temp2, temp3))
    print("Die Durchschnittstemperatur beträgt: {0:.2f} °C".format(durchschnitt))
except Exception as e:
    print("keine kommas ! Punkt ! \n" + e.args[0])
