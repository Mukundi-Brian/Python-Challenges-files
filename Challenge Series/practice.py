# Practice series
# ************************* ------------------------------
# Phase 1: (Variables, set, tuple, dict, 2d collections)
# ************************* ------------------------------

# Exercise 1: Shopping cart program

# my_shop_dict = {
#     "Soap": 3.50,
#     "Bread": 1.90,
#     "Milk": 5.50,
#     "Oil": 10.50
# }

# user_total_cost = []
# final_bill = None
# user_cart = {}

# is_shopping = True

# while is_shopping:
#     print("-----------------Shop Items-------------------")
#     for key, value in my_shop_dict.items():
#         print(f"{key} : ${value:.2f}")
#     user_choice = input("Enter the name of the product to purchase(q to quit): ").strip().capitalize()
#     if user_choice == "Q":
#         print("Exiting program, thank you for shopping, come again.")
#         is_shopping = False
#     elif user_choice not in my_shop_dict:
#         print("Item not found")
#         continue
#     elif user_choice in my_shop_dict:
#         print(f"'{user_choice}' successfully added to cart")
#         user_total_cost.append(my_shop_dict[user_choice])
#         user_cart[user_choice] = my_shop_dict[user_choice]
#         print("------------Your Cart-------------")
#         for items, price in user_cart.items():
#             print(items, end=", ")
#         print()
#         continue_shopping = input("Do you want to continue shopping? (y/n): ").strip().lower()
#         if not continue_shopping == "y":
#             print("Exiting program, thank you for shopping, come again.")
#             is_shopping = False
#         else:
#             continue

# final_bill = sum(user_total_cost)

# if final_bill:
#     print("Thanks for shopping with us:")
#     print("---------------Your Order-----------------")
#     for item, price in user_cart.items():
#         print(f"{item} : ${price:.2f}")
#     print(f"Total cost is: ${final_bill:.2f}")


# Exercise 2: 2D grid printer
# total_sum = 0
# for row in range(1, 4):
#     for col in range(1, 4):
#         total_sum += col
#         print(col, end=" ")
#     print()

# print(f"Total Sum: {total_sum}")


# Exercise 3: Filter with sets

# list_1 = [1, 1, 3, 4, 5, 1, 2, 5, 5, 9]
# list_2 = [1, 2, 3, 6, 7, 8, 10, 4, 6, 8]

# set_1 = set(list_1)
# set_2 = set(list_2)
# # print(list_1)
# # print(list_2)

# for num in set_1 & set_2:
#     if (num % 2 == 0):
#         print(num, end=", ")
# print()

# # Exercise 2 Fixed: 2D Grid Printer
# grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# total_sum = 0

# print("--- 2D Grid ---")
# # Outer loop goes through each row
# for row in grid:
#     # Inner loop goes through each item in the row
#     for num in row:
#         print(num, end=" ")
#         total_sum += num
#     print() # New line after each row

# print(f"Total Sum: {total_sum}")









# ************************* ------------------------------
# Phase 2 (Functions, Arguments (*args, **kwargs), Format specifiers, list comprehensions, Match case)
# ************************* ------------------------------

# Exercise 1: Flexible Multiplier (Args & Kwargs)

# Build profile (**kwargs)

# def build_profile (**kwargs):
#     return "\n".join([f"{key}: {value}" for key, value in kwargs.items()])
    
# print(build_profile(name = "Gumball", age = 14, country = "Elmore"))

# Multiply_all(*args)

# import math

# def multiply_all(*args):
#     if not args:
#         return "Nothing to Multiply!"
    
#     return math.prod(args)

# print(multiply_all(2, 13))

# Exercise 2: List Comprehension
# numbers = []
# for num in range(1, 21):
#     numbers.append(num)

# Learnt a faster way
# numbers = list(range(1, 21))
# print(numbers)

# # print(numbers)
# num_div_by_3 = [num ** 2 for num in numbers if num % 3 == 0]
# print(num_div_by_3)

# number = 3345798
# sum_of_num = 0
# for i in str(number):
#     sum_of_num += int(i)
#     print(i)

# print(sum_of_num)
# print("Num is divisble" if sum_of_num % 3 == 0 else "None")
# print(f"Num is divisible by 3 because total sum of numbers: {sum_of_num} is divisble by 3")

# Fizz Buzz test
# For a list of numbers, if num is divisble by 3 print "Fizz" if by 5 print "Buzz", by both "FizzBuzz"

# numbers = list(range(1, 21))

# for num in numbers:
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz", end=", ")
#     elif num % 3 == 0:
#         print("Fizz", end=", ")
#     elif num % 5 == 0:
#         print("Buzz", end=", ")
#     else:
#         print(num, end=", ")

# Sub_Exercise 1: Looping and counting evens and odds
# even_nums = 0
# odd_nums = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_nums += 1
#     else:
#         odd_nums += 1

# print(f"In a list (1-20), there are {even_nums} even numbers and {odd_nums} odd numbers")

# Sub_Exercise 2: masking passwords

# card_number = "453271829381"
# last_digits = card_number[-4:]
# hidden_password = ""
# hidden_password = "*" * len(card_number[:-4])

# print(" ".join(hidden_password + last_digits))

# for num in card_number[:-4]:
    # hidden_password += "*"

# print(hidden_password + last_digits)
# Sub_Exercise 3: "bizzbang" multipliers

# for num in range(1, 31):
#     if num % 28 == 0:
#         print("BizzBang", end=" ")
#     elif num % 7 == 0:
#         print("Bang", end=" ")
#     elif num % 4 == 0:
#         print("Bizz", end=" ")
#     else:
#         print(num, end=" ")

# Sub_Exercise 4: Flexing list comprehension

# my_list = [2, 5, 9, 12, 15, 18, 21]

# new_list = []

# for num in my_list:
#     if num % 2 == 0:
#         new_value = num * 10
#         new_list.append(new_value)
#     else:
#         new_list.append(num)

# new_list = [num * 10 for num in my_list if num % 2 == 0]
# new_list = [num * 10 if num % 2 == 0 else num for num in my_list]

# print(new_list)

# Sub_Exercise 6: VIP filtering
# ages = [14, 22, 18, 30, 16, 25, 41, 12]

# approved_ages = [age for age in ages if age >= 18]

# print(approved_ages)

# Sub_Exercise 7: Price doubler
# prices = [10, 5, 20, 3, 50]

# new_prices = [price * 2 if price < 15 else price for price in prices]

# print(new_prices)

# Sub_Exercise 8: username cleaning
# users = ["  alice ", "bob  ", " CHARLIE ", "delta"]

# formatted_usernames = [user.strip().lower() for user in users]

# print(formatted_usernames)

# Exercise 3: Match_case checker -----------

# def day_checker (day_of_week):
#     match day_of_week:
#         case "Monday":
#             return "It is a weekday"
#         case "Tuesday":
#             return "It is a weekday"
#         case "Wednesday":
#             return "It is a weekday"
#         case "Thursday":
#             return "It is a weekday"
#         case "Friday":
#             return "It is a weekday"
#         case "Saturday":
#             return "It is a weekend"
#         case "Sunday":
#             return "It is a weekend"
#         case _:
#             return f"'{day_of_week}' is not a valid day!"

# def day_checker (day_of_week):
#     match day_of_week:
#         case "Monday" | "Tuesday" | "Wednesday"| "Thursday"| "Friday":
#             return "It is a weekday"
#         case "Saturday" | "Sunday":
#             return "It is a weekend"
#         case _:
#             return f"'{day_of_week}' is not a valid day!"

# # print(day_checker("Friday"))










# ************************* ------------------------------
# Phase 3 (Scope Resolution, Modules, Understanding if dunder name == dunder main)
# ************************* ------------------------------

# Exercise 1: Scope Resolution ------------

# Global Variable
# score = 100

# def get_score():
#     # local variable
#     global score
#     score = 50
#     return f"The score is: {score}"

# print(get_score())

# Exercise 2: Modules ------------

# import helpers

# my_temp_in_fahrenheit = 100

# my_temp_in_celsius = helpers.convert_temp(my_temp_in_fahrenheit)
# my_bmi = helpers.body_mass_index(58, 168)

# print(my_temp_in_celsius)
# print(my_bmi)

# Exercise 3: Understanding if dunder name == dunder main ------------

# print(helpers)







# ************************* ------------------------------
# Phase 4: (class, instance, class_variables)
#          (inheritance, super())
#          (Method overriding and duck typing)
# ************************* ------------------------------

# class Robot:
#     # class variable
#     population = 0

#     def __init__(self, name, battery):
#         self.name = name
#         self.battery = battery
#         Robot.population += 1

#     # Speaking function
#     def speak(self):
#         print("Beep Boop")

# my_robot = Robot("Simon", 90)

# class CleaningRobot(Robot):
#     # Inheriting from robot: Name and battery
#     # super().__init__(name, battery)

#     # Cleaning method
#     def clean(self):
#         print(f"'{self.name}' is cleaning.")
#         self.battery -= 50

#     # Speaking function
#     def speak(self):
#         print("I am cleaning the floor.")

# print(my_robot.battery)
# robot_2 = CleaningRobot("Finn", 90)

# robot_2.clean()
# print(robot_2.battery)
# robot_2.speak()






# ************************* ------------------------------
# Phase 5: (Decorators,
# ************************* ------------------------------

# Execution Timer Decorator *********************
# Imports
# import time
# import functools

# Measuring time decorator
# def measure_time(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         time_taken = end_time - start_time
#         print(f"Execution Time: {time_taken:.2f}")
#         return result
#     return wrapper

# @measure_time
# def simulate_spatial_query(points_count):
#     print(f"Processing {points_count} spatial points...")
#     time.sleep(2) # simulating the time taken
#     return f"Success: Processed {points_count} spatial points"

# print(simulate_spatial_query.__name__)
# print(simulate_spatial_query(300))


# # Validator (Bouncer) Decorator *********************
# import functools

# def validate_positive(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             # Can also be done like this
#             # if isinstance(arg, (int, float)) and arg <= 0:
#             #     raise ValueError("Error!, Can't execute buffer with radius of 0 or less than 0")
#             if arg <= 0:
#                 raise ValueError("Error!, Can't execute buffer with radius of 0 or less than 0")
#         for value in kwargs.values():
#             # Can also be done like this:
#             if isinstance (value, (int, float)) and value <= 0:
#                 raise ValueError("Error!, Can't execute buffer with radius of 0 or less than 0")
#             # if value <= 0:
#             #     # raise ValueError("Error!, Can't execute buffer with radius of 0 or less than 0")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper

# # Retry function
# # def retry_code(func):
# #     @functools.wraps(func)
# #     def wrapper(*args, **kwargs):
# #         retry_times = 2
# #         try:
# #             result = func(*args, **kwargs)
# #             return result
# #         except ValueError as e:
# #             print("Raised ValueError", e)
# #             for i in range(retry_times):
# #                 print(f"{i}. Trying again...")
# #                 result = func(*args, **kwargs)
# #             return result
# #         except ConnectionError as c:
# #             print("Raised ValueError", c)
# #             for i in range(retry_times):
# #                 print(f"{i}. Trying again...")
# #                 result = func(*args, **kwargs)
# #             return result
# #     return wrapper

# # That retry code was good however it there's a better way to reimplement it rather than hardcoding a fixed number of retries

# def retry_code(max_attempts=3):
#     if max_attempts <= 0:
#         # print(f"Warning! Invalid max attempts: '{max_attempts}' setting to default max_attempts(3)")
#         # max_attempts = 3
        
#         #instead of printing an error, raise it just in case the user didn't want a default fallback
#         raise ValueError(f"Max attempts must be at least 1, got {max_attempts}")
#     def decorator_for_retrying(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             attempts = 0
#             while attempts < max_attempts:
#                 try:
#                     result = func(*args, **kwargs)
#                     return result
#                 except ConnectionError as e:
#                     attempts += 1
#                     if attempts >= max_attempts:
#                         print("[FATAL] Max retry attempts reached. Crashing!")
#                         raise
#                     else:
#                         print(f"[RETRYING] failed. Attempted '{attempts}' time(s): {e}")
#         return wrapper
#     return decorator_for_retrying

# @retry_code(max_attempts=1)
# @validate_positive
# def calculate_buffer_zone(radius):
#     return f"Buffer zone created with radius: {radius} km"

# # print(calculate_buffer_zone(12))

# # # This should not work
# # try:
# #     print(calculate_buffer_zone(-12))
# # except ValueError as e:
# #     print("Caught! by decorator:", e)

# # try:
# #     print(calculate_buffer_zone(radius=12))
# # except ValueError as e:
# #     print("Caught!", e)
# # except ConnectionError as c:
# #     print("Caught!", c)
# print(calculate_buffer_zone(radius=12))



# Final Boss Challenge -----*********************
# Autonomous Delivery Drone
# A python script that models an autonomous delivery drone
# Imports
import time
import functools
class DroneLocation():
    """Tracks the drone location"""
    def __init__(self, latitude:float, longitude:float):
        self.latitude = latitude
        self.longitude = longitude

    # Static method for checking valid latitude
    @staticmethod
    def is_valid_latitude(latitude):
        """Checks for valid latitude"""
        # time.sleep(1)
        return -90 <= latitude <= 90

    # static method for checking valid longitude
    @staticmethod
    def is_valid_longitude(longitude):
        """Checks for valid longitude"""
        # time.sleep(1)
        return -180 <= longitude <= 180

    # setting up latitude
    @property
    def latitude(self):
        """Introduces a security check on latitude"""
        # time.sleep(2)
        return self._latitude

    @latitude.setter
    def latitude(self, new_latitude):
        if not self.is_valid_latitude(new_latitude):
            raise ValueError(f"Latitude value out of range, expected (-90, 90), got ({new_latitude})")
        # time.sleep(3)
        self._latitude = new_latitude
    
    # setting up longitude
    @property
    def longitude(self):
        """Introduces a security check on longitude value"""
        # time.sleep(2)
        return self._longitude
    
    @longitude.setter
    def longitude(self, new_longitude):
        if not self.is_valid_longitude(new_longitude):
            raise ValueError(f"Longitude value out of range, expected (-180, 180), got ({new_longitude})")
        # time.sleep(2)
        self._longitude = new_longitude

    # Magic method for inspection
    def __repr__(self):
        # time.sleep(0.5)
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"

    # Magic method for comparison of coordinates
    def __eq__(self, other):
        # time.sleep(0.5)
        return self.latitude == other.longitude and self.longitude == other.longitude       

# Tracks execution time
def log_telemetry(func):
    """Tracks execution time every time a drone method executes"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        print(f"Time taken is: {time_taken}")
        return result
    return wrapper

class DeliveryDrone():
    """Main delivery drone class"""
    def __init__(self, drone_id, battery_level, payload_kg):
        self.drone_id = drone_id
        self.battery_level = battery_level
        self.payload_kg = payload_kg

location1 = DroneLocation(20, 1119)

print(location1)
