#!/usr/local/bin/python3

# 2. Calculati suma numerelor pare mai mici decit 100.
n = 1
suma = []
while n < 100:
   
    if n % 2 == 0:
        suma.append(n)
    n +=1
    
print(sum(suma))

