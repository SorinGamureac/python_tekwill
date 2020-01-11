#a = [1,2,4]
#print("1" == 1)
#print((1 + 2 == 3) or (10 < 20) and (77 + 8) and 7 in a)
#print((False or (True and False)))
#print(7 and False
#print(3 < 3 and 3 <= 3)
#print(7 < 7 or 3 >= 3)

import copy

# a = [1, 2, [2, 3]]
# b = copy.copy(a)
# print(a[2] is b[2])

# c = copy.deepcopy(a)
# print(a[2] is c[2])

# a = {"name": "Alice", "age": 44, "profile":{"occupation": "student"}}
# b = copy.copy(a)
# c = copy.deepcopy(a)
# print(a is b)
# print(a["profile"] is b["profile"])
# print(a["profile"] is c["profile"]) 

# if True:
#     print("yes")
#     print("here")

# if []:
#     print("tralala")
# if True:
#     print("bbb")
# else: 
#     print("miau")

fisier_cu_extensie = input("Introduceti denumirea fisierului cu extensie ")
x = fisier_cu_extensie.split('.')
print(x)

if len(fisier_cu_extensie) == 1:
    print("fisierul nu are extensie")
elif x[-1] == 'py':
    print(f'(acest fisier are extensia py')
else:
    print(f"Acest fisier are extensia {x[-1]}")

