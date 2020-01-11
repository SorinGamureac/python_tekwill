#!/usr/local/bin/python3
from base_test import Zoo
                
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
        






