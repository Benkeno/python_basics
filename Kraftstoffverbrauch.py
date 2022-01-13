print('Das ist ein Programm zur Kraftstoff Verbrauchsberechnung')
print('Gefahrene Kilometer eingeben: ')
gefahrene_km = float(input())
print('Verbrauchte Liter eingeben: ')
verbrauchte_liter = float(input())
verbrauch_je_km = verbrauchte_liter / gefahrene_km
l_km = verbrauch_je_km * 100.0
print("Es wurden {0:.1f} Liter auf 100km verbraucht".format(l_km) +
      " bei einer Strecke von {0:.1f} KM".format(gefahrene_km))