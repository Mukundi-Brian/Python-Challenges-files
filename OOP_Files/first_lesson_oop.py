# Classes v objects
# Classes = blueprint for object
# Object = a bundle of related attributes and methods eg real life object like car, book, pen

# Let's create a class, for cleaner code and arrangement, let's put classes in a separate file
# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

# Let's import the car class in the new file
from first_lesson_car import Car

car1 = Car("Pagani", 2025, "indigo", True)
car2 = Car("GLE 63s", 2026, "Red", False)
car3 = Car("Xiaomi Yu7 GT", 2028, "Wine Red", False)
car4 = Car("Chevy Malibu", 2020, "Violet", True)

print(car1.model)
print(car1.for_sale)
print(car4.model)
car4.drive()
car2.stop()
car2.describe()
car3.describe()
car1.drive()