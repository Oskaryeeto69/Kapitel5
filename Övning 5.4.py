# B, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v,w, x, och z.
# A, e, i, o, u, y, å, ä och ö.

vokal = "aeiouyåäö" # säger vilka bokstäver som är vokaler
konsonanter = "bcdfghjklmnpqrstvwxz" # säger vilka bokstäver som är konsonanter
userString = input("Skriv en mening: ") # ber användaren att skriva en mening

# Hohejoj! Kokomom inon,

newString = "" # gör en ny string

for c in userString:
    if konsonanter.find(c.lower()) != -1: # letar efter konsonanter och gör nåt coolt xd
        newString += f"{c}o{c.lower()}" # lägger till ett o mellan varje konsonant som hittas
    else: 
        newString +=  # säger att annars ska den låta bokstaven va

print (f"\n{newString}") # printar den nya stringen efter den varit inne i loopen typ