"Scrieti o functie care sa gaseasca maximum a 3 numere"

def maximum(num1, num2, num3):
    if num1 > num2 and num3:
        print(num1)
    elif num2 > num1 and num3:
        print(num2)
    else:
        print(num3)
maximum(6,3,5)