

print("Ohmsche Last ausrechnen")
print("Bitte Spannung eingeben")

V = float(input("Volt: "))
    
print("Bitte Stromstärke eingeben")
    
A = float(input("Ampere: "))
ohm = V / A

print("Der Widerstand R ist {0:.2f} OHM".format(ohm))
