# class Complex:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __mul__(self, other):
#         a = self.a * other.b
#         b = self.b * other.b


# class Parent:
#     def implicit():
#         print("Implicit method")

#     def override(self):
#         print("Parent Method")

#     def altered(self):

# class Child(Parent):
#     def override(self)
#         print("child method")


class Car:
    def __init__(self, color, age, fuel_type="n/a"):
        self.color = color
        self.age = age


    countelectric = 0
    countdiesel = 0

class ElectricCar(Car):
    def __init__(self, age, color, fuel_type="electric"):
        super().__init__(age, color, fuel_type)
        Car.countelectric += 1

        
                

class DieselCar(Car):
    def __init__(self, fuel_type="diesel"):
        super().__init__(self, fuel_type)

print(Car.countelectric)
print(Car.countdiesel)
