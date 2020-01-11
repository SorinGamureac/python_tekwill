# Scrieti un program care sa calculeze suma numerelor pare dintr-o lista, folositi
# functiile reduce / filter
from functools import reduce

a = list([x for x in range(21)])
b = filter(lambda x: x % 2 == 0, a)
c = reduce(lambda x, y: x + y, b)
print(c)

