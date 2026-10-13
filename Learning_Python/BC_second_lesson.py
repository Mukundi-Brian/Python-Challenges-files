# C_stand program, Functions, default arguments, keyword arguments, *args & **kwargs, iterables

# Concession stand program

# menu = {"Pizza": 3.00,
#         "Fries": 1.90,
#         "Popcorn": 0.50,
#         "Soda": 3.00,
#         "Donuts": 1.50,
#         "Chicken": 12.30,
#         "Milk": 5.67,
#         "Chips": 2.50
#         }

# cart = []
# total = 0

# print("----------MENU------------\n")
# for key, value in menu.items():
#     print(f"{key:10}: $ {value:.2f}")
# print("------------------------------")

# while True:
#     food = input("Enter a food (q to quit): ").capitalize()
#     if food.lower() == "q":
#         break
#     elif food in menu:
#         cart.append(food)
#     elif food not in menu:
#         print("------------------------------")
#         print("Food currently unavailable.")
#         print("Please choose something from the menu.")
#         print("------------------------------")

# print()
# print("-------------YOUR ORDER----------------")     
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")

# print()
# print(f"Total is: $ {total:.2f}")

# Functions: default arguments

# Default Arguments
# Default Arguments = A default value for certain parameters.
#                   - Default is used when that argument is omitted
#                   - Makes your function more flexible, reduces # of arguments
#                   1. positional, 2. DEFAULT, 3. Keyword, 4. arbitrary

# def net_price (list_price, discount = 0, tax = 0.05):
#     return list_price * (1-discount) * (1 + tax)


# # print(net_price(500))
# # print(net_price(500, 0.1))
# print(net_price(500, 0.1, 0))

# count up timer

# import time

# def count(end, start = 0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")

# # count(1, 10)
# # count(10)

# Keyword Arguments
# Keyword Arguments = an argument preceded by an identifier
#                   - Helps with readability
#                   - Order of arguments doesn't matter
#                   1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")

# # hello(greeting="Bonjour", title="Regent", first="Ferda", last="Valdrova")
# # hello(first="Ferda", greeting="Bonjour", last="Valdrova", title="Regent")

# for x in range(1, 11):
#     print(x, end=" ") end is a keyword argument

# print("1", "2", "3", "4", "5", sep="-") Sep is a keyword argument

# Exercise: Phone number gen
# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country = 254, area = 123, first = 456, last = 789)

# print(phone_num)

# *args and **kwargs
# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
#          * unpacking operator
#          1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# Arbitrary = meaning a varying amount of arguments, we don't know how many a user will invoke

# def add(*args):
#     # print(type(args))
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# def add(*nums):
#     # print(type(args))
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(2, 4))

# print(add(3,5,5,5,6,7,6,56,76,6,90,6))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Regent", "Ferda", "Valdrova")

# Kwargs

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(street = "567 Skibidi",
#               city = "Hestia",
#               state = "Empire",
#               zip = "1234"
#               )

# Exercise:
# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end =" ")
#     print()

#     if "apt" in kwargs:
#         print(f"{kwargs.get('street')}, {kwargs.get('apt')}")
#     else:
#         print(f"{kwargs.get('street')}")
#     print(f"{kwargs.get('city')}, {kwargs.get('zip')},")

# shipping_label("Dr", "Burnell","William",
#                street = "1 Valdrova Estate",
#                apt = "Castle",
#                city = "Hestia",
#                zip = "1111"
#                )

# Iterables in python
# Iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop

# numbers = [1, 2, 3, 4, 5]
# numbers = (1, 2, 3, 4, 5)

# for num in numbers:
#     print(num, end=" ")

# fruits = {"apple", "banana", "coconut", "lemon"}

# for fruit in fruits:
#     print(fruit)

# my_dict = {
#     "A": 1,
#     "B": 2,
#     "C": 3,
#     "D":4
# }

# for key in my_dict.keys():
#     print(key)

# for value in my_dict.values():
#     print(value)
