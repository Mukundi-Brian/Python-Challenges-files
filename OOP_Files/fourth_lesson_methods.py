# Static methods, class methods, magic methods, property, decorators

# Static methods = A method that belongs to a class rather than any object from that class
#                  (instance)
#                  usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

# class Employee:

#     def __init__(self, name, job_position):
#         self.name = name
#         self.job_position = job_position

#     def get_info(self):
#         # this is an instance method
#         return f"{self.name} = {self.job_position}"

#     @staticmethod
#     def is_valid_position(job_position):
#         valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
#         return job_position in valid_positions


# employee_1 = Employee("Ferda", "Regent")
# employee_2 = Employee("Isabella", "Manager")
# employee_3 = Employee("Burnell", "Cook")
# print(Employee.is_valid_position("Regent"))

# print(employee_1.get_info())
# print(employee_2.get_info())
# print(employee_3.get_info())

# Class methods
# Class methods = allows operations related to the class itself
#                 Take(cls) as the first parameter, which represents the class itself

# class Student:

#     count = 0
#     total_gpa = 0

#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa

#     # Instance method
#     # self refers to any object created from that class
#     def get_info(self):
#         return f"{self.name} {self.gpa}"

#     @classmethod
#     def get_count(cls):
#         return f"Total no of students: {cls.count}"

#     @classmethod
#     # cls refers to class not any object
#     def get_average_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"The average gpa is: {(cls.total_gpa / cls.count):.2f}"

# student1 = Student("Burnell", 4.0)
# student2 = Student("Ferda", 3.5)
# student3 = Student("Hansen", 2.8)

# print(Student.get_count())
# print(student1.get_info())
# print(student2.get_info())
# print(student3.get_info())
# print(Student.get_average_gpa())


# Magic methods
# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                They are automatically called by many of python's built-in operations
#                They allow developers to define or customize the behavior of objects

# class Book:

#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __str__(self):
#         return f"'{self.title}' by {self.author}"

#     # Two parameters since we want to compare two objects
#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author

#     def __lt__(self, other):
#         return self.num_pages < other.num_pages

#     def __gt__(self, other):
#             return self.num_pages > other.num_pages

#     def __add__(self, other):
#          return f"{self.num_pages + other.num_pages} pages"

#     def __contains__(self, keyword):
#          return keyword in self.title or keyword in self.author

#     def __getitem__(self, key):
#         if key == "title":
#               return self.title
         
#         elif key == "author":
#             return self.author
         
#         elif key == "num_pages":
#               return self.num_pages

#         else:
#              return f"Key {key} was not found"
    
# book1 = Book("Abroad in Japan", "Chris Broad", 350)
# book2 = Book("Can't Hurt Me", "David Goggins", 267)
# book3 = Book("Law of Human Nature", "Robert Greene", 750)
# book4 = Book("Law of Human Nature", "Robert Greene", 450)

# print(book1)
# print(book2)
# print(book3)

# print(book3 == book4)
# print(book2 < book1)
# print(book3 > book1)
# print(book2 + book1)

# # print("Human" in book4)
# print(book1['title'])
# print(book1['author'])
# print(book3['audio'])
# print(book2['num_pages'])


# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#   Benefit: Add additional logic when read, write or delete attributes
#   Gives you getter, setter, and deleter method

# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         return f"{self._width} cm"

#     @property
#     def height(self):
#         return f"{self._height} cm"

#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Width must be greater than zero")

#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print("Height must be greater than zero")

#     @width.deleter
#     def width(self):
#         del self._width
#         print("Width has been deleted")

#     @height.deleter
#     def height(self):
#         del self._height
#         print("Height has been deleted")

# rectangle1 = Rectangle(3,4)

# print(rectangle1._width)
# print(rectangle1._height)

# rectangle1.width = 12
# rectangle1.height = 5

# del rectangle1.width
# del rectangle1.height

# print(rectangle1.width)
# print(rectangle1.height)


# Decorator = A function that extends the behavior of another function
#           without modifying the base function
#           pass the base function as an argument to the decorator
# 
#           @ add_sprinkles
#           get_ice_cream("Vanilla")

# def add_sprinkles(function):
#     # Prevents calling of the add sprinkles function unnecessarily
#     def wrapper(*args, **kwargs):
#         print("* You add sprinkles 🎊*")
#         function(*args, **kwargs)
#     return wrapper

# def add_fudge(function):
#     def wrapper(*args, **kwargs):
#         print("*You add fudge 🍫*")
#         function(*args, **kwargs)
#     return wrapper

# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
#     print(f"Here is your {flavor} ice cream 🍨")

# get_ice_cream("vanilla")
