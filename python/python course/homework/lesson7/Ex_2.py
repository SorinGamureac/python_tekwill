#Scrieti un functie generator care sa lucreze ca functia enumerate (yield)
#         b = iter(a)
#         print(next(b))
def generator_yield(it):
    while True:
        try:
            b = iter(it)
            iterable = next(b)
        except StopIteration:
            break
        print(iterable)
g = generator_yield([x for x in range(10)])
