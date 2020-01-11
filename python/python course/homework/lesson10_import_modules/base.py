#!/usr/local/bin/python3
# import Birds
from Animals import birds
# from .fishes import Fishes
# from .mammals import Mammals
# from .reptile import Reptiles

class Zoo:
    
    dict_species = {}
    mammals = 0
    birds = 0
    fishes = 0
    reptiles = 0
    other = 0
    def __init__ (self, age, name, species_class, food=""):
        self.age = age
        self.name = name 
        self.species_class = species_class
        self.food = food
        self.species()
        self.listofanimals()

# if __name__ == "__main__":
#     somon = Fishes(1, "vasea", "fishes")
#     reptilie = Reptiles(1, "sarpe")
#     print(Zoo.somon)

