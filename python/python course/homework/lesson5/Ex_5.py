
#5. Calculati suma toturor numerelor intre 1000 si 2300 care se impart fara rest la
#5 si 7.

#EX 5
q = []
for i in range(1000,2300):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
        q.append(i)
print(sum(q))


