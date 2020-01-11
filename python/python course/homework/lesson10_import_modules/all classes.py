#!/usr/local/bin/python3

from datetime import datetime

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
    
    

    def printspecies(self):
        print(dict_species['reptilie'])

    def species(self):
        if self.species_class == "mammals":
            Zoo.mammals +=1 
        elif self.species_class == "birds":
            Zoo.birds +=1
        elif self.species_class == "fishes":
            Zoo.fishes +=1
        elif self.species_class == "reptiles":
            Zoo.reptiles +=1
        else:
            Zoo.other +=1

        
                
    

    @classmethod
    def init_by_date(cls, name, speciesGroup, bday):
        return cls(name, speciesGroup, datetime.today().year - datetime.strptime(bday, '%Y%m%d').year )

    def __str__(self):
        return f'{self.__class__}({self.name}, {self.speciesGroup}, {self.age})'


class Mammals(Zoo):
    def __init__(self, age, name, species_class="mammals", food=""):
        inst = super().__init__(age, name, species_class, food)
        if 'mamals' in Zoo.dict_species:
            Zoo.dict_species['mamals'].append(inst)
        else:
            Zoo.dict_species['mamals'] = [inst]

    @staticmethod
    def favourite_food():
        print("Mammals' favourite food: \
                \n  -Meet and plants" )


class Birds(Zoo):
    def __init__(self, age, name, species_class="birds", food=""):
        super().__init__(age, name, species_class, food)

    @staticmethod
    def favourite_food():
        print("Birds' favourite food: \
                \n  -Insects, worms, and grubs \
                \n  -Seeds, grasses, and plant material \
                \n  -Nectar and pollen" )

class Fishes(Zoo):
    def __init__(self, age, name, species_class="fishes", food=""):
        super().__init__(age, name, species_class, food)
        
    def favourite_food():
        print("Fishes' favourite food:")
                
class Reptiles(Zoo):
    def __init__(self, age, name, species_class="reptiles", food="", color=""):
        super().__init__(age, name, species_class, food)
        self.color = color
    
    @staticmethod
    def favourite_food():
        print("Reptiles' favourite food: \
                \n  -Animal and plant matter, including fruits and vegetables" )

    def color(self, color='Blue'):
        self.color = color
        print("{self.color}")
        



somon = Fishes(1, "vasea", "fishes")
reptilie = Reptiles(1, "sarpe")
print(Zoo.dict_species)



