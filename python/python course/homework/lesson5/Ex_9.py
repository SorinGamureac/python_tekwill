
#9. Scrieti un program care calculeaza frecventa cu care apare un cuvint intr-o
#propozitie.


#ex 9
propozitie = "la multi ani, la multi ani 43 542 4 43."
p = propozitie.split()
# counts = {}
print(p)
for c in p:
    if c in counts:
        counts[c] += 1
    else:
        counts[c] = 1
print(counts)
