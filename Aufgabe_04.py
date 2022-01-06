"""
Meter pro Nano sekunde in Km pro sekunde umrechnen
"""


lichtJeNanoSek = 0.299792458                    # Lichtgeschwindigkeit in meter pro nanosekunde (1000000) millionstel

lichtJeSekunde = lichtJeNanoSek * 1000 * 1000   # Umrechnung *1000 von meter auf Kilometer pro nanosekunde, dann *1000 von nanosekunde auf sekunde,

print(lichtJeSekunde)