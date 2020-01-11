# exercise 1
a = 10 
a += len(str(a)) 
a = str(a)
print(a)

# exercise 2
n = 2
#eroare = "In padurea cu alune aveau casa" + 2 + "pitici" 
corect_1 = "In padurea cu alune aveau casa 2 pitici"
corect_2 = "In padurea cu alune aveau casa {} pitici".format(n)
print(corect_2)
corect_3 = "In padurea cu alune aveau casa" + " " + str(2) + " " + "pitici"
print(corect_3)
print(f"In padurea cu alune aveau casa {n} pitici")

# exercise 3 - Chestionar
print ("Salut, daca esti student completeaza te rog urmatorul chetionar")
prenume = input("Ce prenume ai? ")
nume = input("Ce nume ai? ")
varsta = int(input("Ce varsta ai? - doar cifra "))
ocupatie = input("Ce ocupatie ai? ")
print("{} {} are varsta de {} ani si el este {}".format(prenume, nume, varsta, ocupatie))

