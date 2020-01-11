#!/usr/local/bin/python3
from base_test import Zoo
class Birds(Zoo):
    def __init__(self, age, name, species_class="birds", food=""):
        super().__init__(age, name, species_class, food)

    @staticmethod
    def favourite_food():
        print("Birds' favourite food: \
                \n  -Insects, worms, and grubs \
                \n  -Seeds, grasses, and plant material \
                \n  -Nectar and pollen" )