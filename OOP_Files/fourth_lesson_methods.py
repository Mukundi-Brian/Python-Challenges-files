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
