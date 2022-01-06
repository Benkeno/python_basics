bakterien =  118                                        # Bakterienanzahl
steigerung = 18                                         # Vermehrung in %
tag = 0                                                 # Tageszähler
grenzwert =  2000                                       # Grenzwert
bakzahler =  0                                          # Variable zur Speicherung der täglichen Bakterienzahl

while bakterien < grenzwert:                            # solange bakterien kleiner als grenzwert
    tag = tag + 1                                       # zähle Tag hoch um + 1
    bakzahler = bakterien + (bakterien / 100 * steigerung)   # bakzähler befüllen mit bakterien + steigerung
    bakterien = bakzahler                                      # neue bakterien nehmen wert aus bakzähler an
    print("Tag:" ,tag, "Bakterien: ", round(bakterien))
    if bakterien  == grenzwert:                                # wenn neue bakterienzahl gleich grenzwert
        print("Tag:" ,tag, "Bakterien: ", round(bakterien))    # drucke hochgezählten Tag und neuste Bakterienzahl

