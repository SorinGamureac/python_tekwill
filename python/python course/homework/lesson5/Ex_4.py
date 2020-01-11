
#4. Scrieti un program care sa afiseze toti divizorii unui numar intreg.


#EX: 4
a = abs(input("Instroduceti un numar intreg"))
for i in range(1,a+1):
    if a % i == 0:
        print(i)
