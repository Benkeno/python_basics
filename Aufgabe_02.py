# Konverter Celsuis zu Fahrenheit

#----------- Eingabe ------------------------------------

temp = float(input("Bitte gib die Temperatur in Celsius ein: ")) # Deklaration Datenvariable und Typ, user Eingabe

#----------- Verabreitung -------------------------------

fahrenheit = (1.8 * temp) + 32.0     # variable umrechnen, neue variable füllen

#----------- Ausgabe ------------------------------------

print("Das sind {0:.2f}° Fahrenheit".format(fahrenheit))    # Ausgabe auf 2 Kommastellen formatiert