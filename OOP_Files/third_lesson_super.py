# Super, Polymorphism, Duck Typing

# super() = function used within a child class to call methods from a parent class          (superclass). It allows you to extend the functionality of the inherited methods

# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled

#     def describe(self):
#         print(f"It is {self.color} and {'filled' if self.is_filled else 'Not filled'}")

# class Circle(Shape):

#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius

#     def describe(self):
#         print(f"It is a circle with an area of: {3.14 * self.radius * self.radius} cm^2")
#         super().describe()

# class Square(Shape):

#     def __init__(self, color, is_filled, width):
#         super().__init__(color, is_filled)
#         self.width = width

#     def describe(self):
#         print(f"It is a square with an area of: {self.width * self.width} cm^2")
#         super().describe()

# class Triangle(Shape):

#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height

#     def describe(self):
#         print(f"It is a triangle with an area of: {(self.width * self.height) / 2} cm^2")
#         super().describe()

# circle = Circle("Red", False, 5)
# square = Square("Violet", True, 12)
# triangle = Triangle("Yellow", True, 15, 25)

# print(triangle.is_filled)
# print(square.is_filled)
# print(circle.color)
# print(circle.is_filled)

# circle.describe()
# square.describe()
# triangle.describe()

# Polymorphism
# Polymorphism = Greek word that means to "have many forms or faces"
# Poly = many
# Morphe = Form

# Two ways to achieve polymorphism
#   1. Inheritance = an object could be treated of the same type as a parent class
#   2. "Duck typing" = object must have necessary attributes / methods

# # Import to add abstract class
# from abc import ABC, abstractmethod
# class Shape:

#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return (self.base * self.height) / 2

# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         super().__init__(radius)
#         self.topping =topping
        
# shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("Chicken", 15)]

# # In this case the shapes have two "faces" while the pizza class has "three" faces, it is considered a shape, a circle and a pizza

# for shape in shapes:
#     print(f"{shape.area()} cm^2")


# Duck Typing
# Duck Typing = Another way to create polymorphism besides inheritance, Object must have the minimum necessary attributes / methods.
# "If it looks like a duck and quacks like a duck, it must be a duck."

# class Animal:
#     alive = True

# class Dog(Animal):
#     def speak(self):
#         print("Woof!")

# class Cat(Animal):
#     def speak(self):
#         print("Meow!")

# class Car:
#     alive = False
#     def speak(self):
#         print("Honk!")

# animals = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)
