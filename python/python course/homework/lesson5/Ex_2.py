
#2. Scrieti un program care converteste temperatura din grade celsius in farenheit
#si invers (formula: c/5 = f-32/9)

# Celsius To Fahrenheit
celsius = float(input("Introduceti temperatura in celsius: "))
fahrenheit = (celsius * 9.0/5.0) + 32.0
print("Temperatura  fahrenheit este {}".format(fahrenheit))

#Fahrenheit To Celsius
fahrenheit_to_celcius = float(input("Introduceti temperatura in Fahrenheit: "))
celsius_new = (fahrenheit_to_celcius - 32.0) * 5.0/9.0
print("Temperatura  Celsius este {}".format(celsius_new))

