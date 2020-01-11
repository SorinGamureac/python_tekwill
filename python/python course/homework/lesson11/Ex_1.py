#!/usr/local/bin/python3

#"""Write a decorator that will print functions name and it’s attributes on call. Use
#func.__name__ attribute"""

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