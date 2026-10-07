# class variables = shared among all instances of a class
#                  - Defined outside the constructor
#                  - Allows you to share data among all objects created from that class
# It is good practice to access a class variable by the class not any instance of the class

# Instance variable = variable bound to a specific object in a class
#                    - It is unique to each object and can't be shared among objects
#                    - Changes made for one object does not affect all other objects
#                    - Defined inside a constructor

class Student:
    """Class for creating student and demonstrating class variables"""

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
        
student1 = Student("John", 20)
student2 = Student("Doe", 24)
student3 = Student("Mario", 56)
student4 = Student("Steven", 31)
student5 = Student("Eugene", 28)

print(student1.name)
print(student1.age)
print(Student.class_year)

print(Student.num_students)
print(f"Class of {Student.class_year} has {Student.num_students} students")