# Class Variables and inheritance
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

# print(student1.name)
# print(student1.age)
# print(Student.class_year)

# print(Student.num_students)
# print(f"Class of {Student.class_year} has {Student.num_students} students")

# Inheritance = Allows a class to inherit attributes and methods from another class,
#              - It helps with code reusability and extensibility
#              - class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

animal1 = Animal("James")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} Meows!")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} WOOFs!")

class Horse(Animal):
    def speak(self):
        print(f"{self.name} Neighs!")

print(animal1.is_alive)
print(animal1.name)
animal1.sleep()

cat1 = Cat("Ralph")
dog1 = Dog("Bobby")
horse1 = Horse("Jester")

cat1.speak()
dog1.speak()
horse1.sleep()
cat1.eat()
print(cat1.is_alive)
