# B, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v,w, x, och z.
# A, e, i, o, u, y, å, ä och ö.

vokal = "aeiouyåäö"
konsonanter = "bcdfghjklmnpqrstvwxz"
userString = input("Skriv en mening: ")

# Hohejoj! Kokomom inon,

newString = ""

for c in userString:
    if konsonanter.find(c.lower()) != -1:
        newString += f"{c}o{c.lower()}"
    else:
        newString += c

print (f"\n{newString}")