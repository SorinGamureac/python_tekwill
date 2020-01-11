#!/usr/local/bin/python3
import time

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before")
#         func()
#         func()
#         func()
#         print("Something is happening after")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()


# def my_decorator(func):
#     def odd():
#         print('I am odd')
#     return odd
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         execution_time = end - start
#         print(execution_time)
#     return wrappers

# @my_decorator
# def sum_one_million():
#     s = 0
#     for i in range(10000):
#         s +=1
#     return s
# sum_one_million()

def my_decorator(func):
    def wrapper(*arg, **kwarg):
        func_name = func.__name__
        print(arg, kwarg, func_name)
        
        func(*arg, **kwarg)

    return wrapper

@my_decorator
def testfunc(*arg, **kwarg):
    return None
testfunc("mi", "mem")

