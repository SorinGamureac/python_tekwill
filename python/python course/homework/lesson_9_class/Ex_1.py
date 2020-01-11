from datetime import date

class Car:
    def __init__ (self, year, fuel_type, color):
        self.year = year
        self.fuel_type = fuel_type
        self.color = color

    def car_age(self):
        return date.today().year - self.year
        # now_year = 2019
        # self.year = now_year - year
        # print(self.year)

    def new_color(self, color):
        self.color = color
        print(self.color)

nisan = Car(1993, "gsl", "blue")
print(nisan.car_age())