# This file contains classes for the first lesson for OOP

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"Your are driving the {self.model}")
    def stop(self):
        print(f"You have stopped the {self.model}")
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")