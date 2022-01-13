print('Das ist ein Programm zur Kraftstoff Verbrauchsberechnung')
print('Gefahrene Kilometer eingeben: ')
gefahrene_km = float(input('KM: '))

print('Gesamtfassungsvermögen des Tanks eingeben: ')
tank = float(input('Liter: '))

print('Aktuellen Stand eingeben: ')
tank_neu = float(input('Liter: '))

print('Es wurde folgendes eingegeben\n {0} Gefahrene Kilometer\n {1} L Gesamtfassungvermögen\n {2} L Neuer Stand'.format(gefahrene_km, tank, tank_neu))

verbrauchte_liter = tank - tank_neu
print('Es wurden insgesamt {0:.1f} Liter verbraucht'.format(verbrauchte_liter))

verbrauch_je_km = verbrauchte_liter / gefahrene_km
l_km = verbrauch_je_km * 100
print('Das sind {0:.1f} Liter auf 100km'.format(l_km))
