# @zero_divisor_decorator
# def divisor_function(number, divisor):
# return number / divisor
# In case of ZeroDivisionError print a message that Division by 0 is not allowed.

def zero_divisor_decorator_new(func):
    def wrapper(number, divisor):
        if divisor == 0:
            print("Division by 0 is not allowed")
        else:
            divisor_function(number, divisor)
    return wrapper
def divisor_function(number, divisor):
    n = number / divisor
    print(n)
    return n

@zero_divisor_decorator_new
m  = divisor_function(20, 4)
m()