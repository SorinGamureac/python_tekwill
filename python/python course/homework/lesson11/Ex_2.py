#!/usr/local/bin/python3
#Create a decorator that will repeat function execution N times with X seconds
#delay. Use time.sleep() function.
import time
def my_decorator(func):
    def wrapper(r, *arg, **kwarg,):
        print(arg, kwarg)
        for i in range(0,r):
            func(r,*arg, **kwarg)
            time.sleep(5)
    return wrapper

@my_decorator
def testfunc(r, *arg, **kwarg,):
    l = print(*arg, *kwarg)
    return l
testfunc(5, "1", "2", "3", "test", "4")