
# #8. Scrieti un program care verifica daca o parola introdusa de utilizator este
# securizata
# ● Lungimea minima 6 caractere
# ● Cotine cel putin 1 litera in intervalul [a-z]
# ● Cotine cel putin 1 litera in intervalul [A-Z]
# ● Cotine cel putin 1 cifra
# ● Contine cel putin un caracter special [!, /, #]
# ● Nu contine caractere interzire [@, ‘, {, }]

import string
parola = input("introduceti o parola securizata ")
az_lower = string.ascii_letters[:26]
az_upper = string.ascii_letters[26:]
digit = string.digits
special_caracter = ["!", "/", "#"]
faracaractere = ["@", '\"', "{", "}"]

bingo = set()
if len(parola) > 6:
    bingo.add(1)
for p in parola:
    if p in az_lower:
        bingo.add(2)
    elif p in az_upper:
        bingo.add(3)
    elif p in digit:
        bingo.add(4)
    elif p in special_caracter:
        bingo.add(5)
    elif p in faracaractere:
        bingo.add(6)
    else:
        pass
if len(bingo) == 5 and "6" not in bingo:
    print("felicitari")
else: 
    print("introduceti alta parola")
