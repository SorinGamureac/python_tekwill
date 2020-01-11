#!/usr/local/bin/python3
# def my_generator(n):
#     while n<10:
#         yield n
#         n +=1
        
# g = my_generator(0)
# print(g)

# for i in g:
#     print(i)
#http string respons
#generator - accesam o functie
#iter - accesam fiecare element


# import sys

# a = list(range(10000))
# i = iter(range(10000))

# print(sys.getsizeof(a))
# print(sys.getsizeof(i))

# a = {
#     '1': lambda x: x+1,
#     '2': lambda x: x+2,
#     '3': lambda x: x+3
# }

# b = a['2'](1)
# print(b)

# a = [1,2,3,4]
# b = map(lambda x:x+10, a)
# print(type(b))

# for i in b:
#     print(i)

from functools import reduce

a = [1,2,3,4,5,6,7,8]


c = reduce(lambda x,y: x+y, map(lambda x:x*10,filter(lambda x:x % 2 == 0,a)))
print(c)