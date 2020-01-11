#!/usr/local/bin/python3
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


    