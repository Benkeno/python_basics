#die Differenz (-), das Produkt(+), der Quotient (/) und der Divisionsrest (%) von zwei natürlichen Zahlen


#--------- Eingabe -------------------------------- 

zahl1 = int(input("Bitte Zahl 1 eingeben: "))   # Eingabe Zahl 1
zahl2 = int(input("Bitte Zahl 2 eingeben: "))   # Eingabe Zahl 2

#--------- Verarbeitung nach Formeln -------------- 

differenz = zahl1 - zahl2                       # Zahl 1 plus Zahl 2
produkt = zahl1 + zahl2                         # Zahl 1 minus Zahl 2
quotient = zahl1 / zahl2                        # Zahl 1 durch Zahl 2
modulo = zahl1 % zahl2                          # DivRest Zahl 1 durch Zahl 2


#---------- Ausgabe -------------------------------


print("Differenz: ", differenz)                 # Ausgabe int
print("Produkt: ", produkt)                     # Ausgbae int
print("Quotient.4f: {0:.4f}".format(quotient))  # Ausgabe float arraystelle 0 auf 4 stellen komma formatiert 
print("Divisionsrest: ", modulo)                # Ausgabe int Ganze Zahl
print("Quotient.2f: " , "%.2f" % quotient)      # Ausgabe float mit variable formatiert
