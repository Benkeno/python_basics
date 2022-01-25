from random import randint

# 3 Würfel Zufallszahl, 3x Würfe, Summe der 3 Würfel in 3 Würfen
wuerfel1 = randint(1, 6)
wuerfel2 = randint(1, 6)
wuerfel3 = randint(1, 6)
wurf1 = wuerfel1 + wuerfel2 + wuerfel3

wuerfel1 = randint(1, 6)
wuerfel2 = randint(1, 6)
wuerfel3 = randint(1, 6)
wurf2 = wuerfel1 + wuerfel2 + wuerfel3

wuerfel1 = randint(1, 6)
wuerfel2 = randint(1, 6)
wuerfel3 = randint(1, 6)
wurf3 = wuerfel1 + wuerfel2 + wuerfel3

print(wurf1, wurf2, wurf3)
print("Ergebniss: ", wurf1 + wurf2 + wurf3)