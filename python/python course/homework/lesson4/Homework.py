#!/usr/local/bin/python3
# 1
""" Scrieti un program care detecteaza daca un fisier are extensia py.
Daca extensia este diferita de py printati-o pe ecran.
Daca fisierul nu are extensie printati pe ecaran un mesaj de avrtizare.
(Folositi functiile input, split(), conditionale) """

fisier_cu_extensie = input("Introduceti denumirea fisierului cu extensie ")
x = fisier_cu_extensie.split('.')
print(x)
if len(x) == 1:
    print("fisierul nu are extensie")
elif x[-1] == 'py':
    print('acest fisier are extensia py')
else:
    print(f'Acest fisier are extensia {x[-1]} ')



# 2. Calculati suma numerelor pare mai mici decit 100.
n = 1
suma = []
while n < 100:
   
    if n % 2 == 0:
        suma.append(n)
    n +=1
    
print(sum(suma))

# 3 Scrieti un program care converteste temperatura din grade celsius in farenheit
# si invers (formula: c/5 = f-32/9)

# Celsius To Fahrenheit
celsius = float(input("Introduceti temperatura in celsius: "))
fahrenheit = (celsius * 9.0/5.0) + 32.0
print("Temperatura  fahrenheit este {}".format(fahrenheit))

#Fahrenheit To Celsius
fahrenheit_to_celcius = float(input("Introduceti temperatura in Fahrenheit: "))
celsius_new = (fahrenheit_to_celcius - 32.0) * 5.0/9.0
print("Temperatura  Celsius este {}".format(celsius_new))

# 4. Scrieti un program determina daca un text este palindrom (caiac, capac,
# minim)

palindrom = input("Introduceti un cuvant palindrom ")
a  = palindrom[::-1]
if a == palindrom:
    print("Felicitari cuvantul {} este palindrom".format(a))
else:
    print("cuvantul nu este palindrom")
