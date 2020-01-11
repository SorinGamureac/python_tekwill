#!/usr/local/bin/python3 
# Scrieti o functie care primeste la input un text cu cifre si il converteste in numar,
# in caz de exceptie (este introdus o litera), afisati un mesaj de erroare si chemati
# functia de convertire din nou.
import random

with open("countries.txt", "r", encoding="utf-8") as fc:
    data_doc = {}
    for data in fc.readlines():
    #data = fc.readline()
    #datanew = data.split(',')
        # print(data)
        
        lst = data.split(',')
        print(lst)
        lst[-1]=lst[-1].strip()
        # print(lst)
        key, value = lst[0], lst[-1]
        print(key)
        data_doc[key] = value
a = 0 #numar de intrebari
while a<5:
    random_country = random.choice(list(data_doc.keys()))
    random_country_capital = data_doc[random_country]
    multiple = random.choices(list(data_doc.values()), k = 3)
    multiple.append(random_country_capital)
    random.shuffle(multiple)
    dictOfWords = { i : multiple[i] for i in range(0, len(multiple) ) }
    #0print(dictOfWords)
    print(f'Numeste capitala tarii {random_country}?')
    
    try:
        varianta = int(input(f"""Introduceti cifra corecta din variantele de mai jos 
         0 : {dictOfWords[0]}
         1 : {dictOfWords[1]}
         2 : {dictOfWords[2]}
         3 : {dictOfWords[3]}
         ---------------------------
         """))
        if a == 4:
            print("felicitari ai dat raspuns corect la 4 intrebari")
            break
        elif dictOfWords[varianta] == random_country_capital:
            a +=1
            print(f"felicitari ai raspuns corect de {a} ori")
        else:
            print(f"Raspunsul corect este {random_country_capital} ")
    except ValueError:
        print("Introduceti cifra corect")
