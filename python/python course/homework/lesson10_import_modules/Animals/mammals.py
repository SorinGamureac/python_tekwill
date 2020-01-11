#!/usr/local/bin/python3
from base_test import Zoo
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