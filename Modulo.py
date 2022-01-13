print('Das ist ein Programm zur Berrechnung der Ganzzahl')
print('Zu teilende Zahl eingeben:')
zahl = float(input('Zahl'))
print('Ganzzahliger Teiler')
teiler = int(input('Ganze Zahl'))

modulo = zahl % teiler
print("{0:.2f} Moduliert".format(modulo))
