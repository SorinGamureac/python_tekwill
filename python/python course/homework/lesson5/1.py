#1. Calculati suma numerelor pare mai mici decit 100.
2. Scrieti un program care converteste temperatura din grade celsius in farenheit
si invers (formula: c/5 = f-32/9)
3. Scrieti un program determina daca un text este palindrom (caiac, capac,
minim)
4. Scrieti un program care sa afiseze toti divizorii unui numar intreg.
5. Calculati suma toturor numerelor intre 1000 si 2300 care se impart fara rest la
5 si 7.
6. Scrieti un program care sa primeasca la input un numar N intreg si sa creeze
un dictionar care contine numer mai mici sau egale decit N si N*2. Ex(4 - > {1:
1, 2: 4, 3: 9, 4: 16})

1. Scrieti un program care sa calculeze numarul de litere si cifre din un text.
2. Scrieti un program care verifica daca o parola introdusa de utilizator este
securizata
● Lungimea minima 6 caractere
● Cotine cel putin 1 litera in intervalul [a-z]
● Cotine cel putin 1 litera in intervalul [A-Z]
● Cotine cel putin 1 cifra
● Contine cel putin un caracter special [!, /, #]
● Nu contine caractere interzire [@, ‘, {, }]
3. Scrieti un program care calculeaza frecventa cu care apare un cuvint intr-o
propozitie.
4. Scrieti un program care sa elimine cuvinte duplicate dintr-o propozitie.

                                         #!/usr/local/bin/python3

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



                                         
# a = [1, 2, 3, 4]
# j = 0
# for i in a:
#     print(i)
# count = 0
# for i in range(0, 9, 3):

# s = "spam"
# a = enumerate(s)
# for index, i in a:
#     print(index,i)

#EX: 4
# a = abs(input("Instroduceti un numar intreg"))
# for i in range(1,a+1):
#     if a % i == 0:
#         print(i)
#EX 5
# q = []
# for i in range(1000,2300):
#     if i % 5 == 0 and i % 7 == 0:
#         print(i)
#         q.append(i)
# print(sum(q))


# d = {}
# z = abs(input("introduceti un numar intreg"))
# for i in range(z):
#     d.update({i:i*i})
# print(d)

# s = []
# t = []
# d = []
# text = input("introduceti textul")
# for i in text:
#     if i.isdigit():
#         d.append(1)
#     elif i.isalpha():
#         s.append(1)
#     else:
#         t.append(1)
# print(sum(t))
# print(sum(d))
# print(sum(s))


#ex 9
# propozitie = "la multi ani, la multi ani 43 542 4 43."
# p = set(propozitie.split())
# # counts = {}
# print(p)
# for c in p:
#     if c in counts:
#         counts[c] += 1
#     else:
#         counts[c] = 1
# print(counts)


#ex 10
# print(p)
    
import string
#ex 7
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
    print("felichitari")
else: 
    print("introduceti alta parola")
