# Abstract class = a class that cannot be instantiated on its own; Meant to be subclassed.
#      - They can contain abstract methods, which are declared but have no implementation
# Abstract class advantages:
#   1. Prevents instantiation of the class itself
#   2. Requires children to use inherited abstract methods

# To work with abstract classes we need to import ABC
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")
    
    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You drive the bike")
        
    def stop(self):
        print("You stop the bike")

class Boat(Vehicle):
    def go(self):
        print("You sail the boat")
        
    def stop(self):
        print("You anchor the boat")

car1 = Car()
bike1 = Motorcycle()
boat1 = Boat()

car1.go()
boat1.stop()
bike1.stop()
