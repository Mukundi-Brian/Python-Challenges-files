# # This file contains my practice code with OOP in python

# Exercise 1... -----------------

# class Book:
#     # Class variable to check the number of books
#     book_count = 0

#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self._price = price
#         Book.book_count += 1

#     # Magic method -  to change how printing the book works
#     def __str__(self):
#         return f"'{self.title}' by {self.author} - ${self._price}"

#     # class method - to format strings received
#     @ classmethod
#     def from_string(cls, book_string):
#         title, author, price = book_string.strip().split("-")
#         return cls(title, author, float(price))

#     # property - to allow price to be accessed as a normal variable while also protecting it from random changes
#     @ property
#     def price(self):
#         # return f"${self._price}"
#         # Mostly keep the getters pure (Return raw data)
#         return self._price 

#     @price.setter
#     def price(self, new_price):
#         if new_price < 0:
#             print("Error, price cannot be less than zero")
#         else:
#             self._price = new_price
#             return self._price
        
# my_first_book = Book("Abroad in Japan", "Chris Broad", 199.99)
# my_second_book = Book("The Body", "Bill Bryson", 1099.10)

# print(my_first_book)
# # print(my_first_book.from_string("1984-William Shakespeare-1299.50"))
# # Call class methods using the class not instances of the class
# print(Book.from_string("1984-William Shakespeare-1299.50"))
# my_first_book.price = -120.40
# print(my_first_book.price)
# print(Book.book_count)


# Exercise 2... -----------------
# Drone obstacle detection system

# class BoundingBox:
#     # Class variable - to count the number of objects
#     box_count = 0

#     def __init__(self, label:str, confidence:float):
#         self.label: str = label
#         self.confidence: float = confidence
#         BoundingBox.box_count += 1

#     # class method - an alternative constructor
#     @ classmethod
#     def from_csv_output(cls, raw_string: str):
#         label, confidence = raw_string.strip().split(":")
#         return cls(label, float(confidence))

#     # Property method that returns the confidence value and rejects invalid entry
#     @property
#     def confidence(self):
#         return self._confidence

#     @confidence.setter
#     def confidence(self, new_confidence):
#         # if 0 < new_confidence < 1:
#         if new_confidence > 1 or new_confidence < 0:
#             raise ValueError ("Error, Invalid confidence level!")
#         else:
#             # print("New confidence level set")
#             self._confidence = new_confidence

#     # Magic method for printing the objects of the class
#     def __str__(self):
#         return f"{self.label}, confidence level: {self.confidence}"
    
# obstacle_1 = BoundingBox("Car", 0)
# print(BoundingBox.from_csv_output("Pole:0.85"))
# print(obstacle_1)




# Exercise 3... -----------------
# RobotServo - robotic arm joint, can only rotate (0, 180) degrees
# import math
# class RobotServo:
#     # class variable
#     servo_count = 0
#     def __init__(self, angle: float, battery: float):
#         self.angle = angle
#         self.battery = battery
#         RobotServo.servo_count += 1

#     # class method that accepts csv inputs
#     @classmethod
#     def from_string_csv(cls, raw):
#         angle, battery = raw.strip().split(",")
#         angle = float(angle)
#         battery = float(battery)
#         return cls(angle, battery)

#     # class method that returns the number of robot servos
#     @classmethod
#     def get_count(cls):
#         return cls.servo_count

#     # static method that converts degrees to radians
#     @staticmethod
#     def degrees_to_radians(degrees):
#         return degrees * math.pi / 180

#     # static method that checks for valid angles
#     @staticmethod
#     def is_valid_angle(angle):
#          return 0 <= angle < 180
            
#     # Property that returns angle value
#     @property
#     def angle(self):
#         return self._angle

#     # Property setter that checks for correct range
#     @angle.setter
#     def angle(self, new_angle):
#         # The robot servo value 0 is allowed since its the home position but it should not reach 180, the maximum limit
#         if not self.is_valid_angle(new_angle):
#             raise ValueError (f"Angle must be at least 0 and less than 180, got '{new_angle}'")
#         self._angle = new_angle

#     # Property getter for battery that returns value
#     @property
#     def battery(self):
#         return self._battery

#     # Property setter for battery level
#     @battery.setter
#     def battery(self, new_battery_level):
#         if not 0 <= new_battery_level <= 100:
#             raise ValueError (f"Battery must be at least 0 and less than 100, got '{new_battery_level}'")
#         self._battery = new_battery_level

#     # Magic method for printing the objects
#     def __str__(self):
#         return f"The current angle: {self.angle:.2f}, battery level: {self.battery:.2f}"

# servo_1 = RobotServo(130, 50)
# # servo_1.angle = 0
# # print(servo_1.angle)
# # print(servo_1)

# servo_2 = RobotServo(0, 100)

# try:
#     servo_3 = RobotServo(10, 50)
# # except ValueError:
# #     print("Caught!", ValueError)
# except ValueError as e:
#     print("Caught!", e)

# print(servo_1)
# print(servo_2)
# print(servo_3)
# print(RobotServo.from_string_csv("12, 90"))

# print(RobotServo.get_count())

# print(RobotServo.is_valid_angle(8))



# Exercise 4... -----------------
# Gps Coordinate class that takes in gps coordinates to feed to a robot
# latitude (-90, 90), longitude(-180, 180), if invalid raise value error
# class GpsCoordinate:
#     def __init__(self, latitude: float, longitude: float):
#         self.latitude = latitude
#         self.longitude = longitude

#     # Class method for alternative construction
#     @classmethod
#     def from_string(cls, new_coordinates):
#         latitude, longitude = new_coordinates.strip().split(",")
#         latitude = latitude.strip()
#         longitude = longitude.strip()
#         return cls(float(latitude), float(longitude))

#     # static method for checking valid latitude
#     @staticmethod
#     def is_valid_latitude(latitude):
#         return -90 <= latitude <= 90

#     # static method for checking valid longitude
#     @staticmethod
#     def is_valid_longitude(longitude):
#         return -180 <= longitude <= 180

#     # Property that checks and returns latitude
#     @property
#     def latitude(self):
#         return self._latitude

#     # Property for latitude to make sure its valid
#     @latitude.setter
#     def latitude(self, new_latitude):
#         if not self.is_valid_latitude(new_latitude):
#             raise ValueError (f"Value out of range, expected (-90, 90) got '{new_latitude}'")
#         self._latitude = new_latitude

#     # Property that checks and returns latitude
#     @property
#     def longitude(self):
#         return self._longitude
    
#     # Property for longitude to make sure its valid
#     @longitude.setter
#     def longitude(self, new_longitude):
#         if not self.is_valid_longitude(new_longitude):
#             raise ValueError (f"Value out of range, expected (-180, 180) got '{new_longitude}'")
#         self._longitude = new_longitude

#     # Magic method for printing the object
#     def __str__(self):
#         return f"Latitude: {self.latitude:.2f}, longitude: {self.longitude:.2f}"

#     # Magic method for checking equality
#     def __eq__(self, other):
#        return self.latitude == other.latitude and self.longitude == other.longitude

#     # Magic method for representing objects
#     def __repr__(self):
#         return f"GpsCoordinate(latitude={self.latitude}, longitude={self.longitude})"

# coordinate_1 = GpsCoordinate(10, 10)

# print(coordinate_1.latitude)
# print(coordinate_1.longitude)

# try:
#     coordinate_2 = GpsCoordinate(-123, 90)
# except ValueError as e:
#     print("Caught!", e)
# coordinate_2 = GpsCoordinate(10, 20)

# print(coordinate_1 == coordinate_2)

# coordinate_3 = GpsCoordinate(0, 12)



# DECORATORS **********************************
# Exercise 4... -----------------
# Performance time tracker
# Decorators that measures time, can wrap any function, measures how long it takes to run, prints the execution duration, and returns the function's actual result.
# import time
# import functools

# def measure_time(func):
    
