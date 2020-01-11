#!/usr/local/bin/python3
import csv
from datetime import date, timedelta
import random
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# with open('text.csv') as f:
#     csv_reader = csv.reader(f)
#     for line in csv_reader:
#             print(line)

# l = open("text.csv")
# print(l.read())
# print(type(l))

# data = ["lo", "la", "ki", "mi", "fa"]
# with open("writer_csv.csv", "w") as me:
#     csv = csv.writer(me, delimiter = ",")
#     for d in data:
#         csv.writerow(d)
#         print(d)


from urllib.request import urlopen

response = urlopen('http://999.md/')

def z():
    for line in response:
        m = line.decode('utf-8')
        return m
    return m
l = z()
print(l)
import re
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', l)
print("Urls: ",urls)


#When course ends
# date_start = date(2019, 10, 28)
# d_end = date_start + timedelta(weeks=15) + timedelta(days=10)
# date_end2 = date.today()-date_start
# print(date_end2)

# r = random.randrange(0,100,1)  
# print(r)
# questions = input("Gaciti numarul de la 1 la 100? y/n")
# count = 0
# while questions == "y":
#         number = int(input("Care este acest numar? "))
#         count +=1
#         if number == r:
#             print("felicitari este corect")
#             break
#         elif count == 5:
#             print("Ai maxim 5 incercari")
#             break
#         elif number < r:
#             print("numarul introdus este mai mic")
#         else:
#             print("numarul introdus este mai mare")
# if questions == "n":
#     print("papa")
