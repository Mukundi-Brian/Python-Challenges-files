# Membership Operators, list comprehensions, match-case, string methods

# Membership Operators = Used to test whether a value or variable is found in a sequence
#                Which include but not limited to: (string, list, tuple, set or dictionary)
#                       1. in
#                       2. not in

# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")

# students = {"Ferda", "Isabella", "Burnell"}

# student = input("Enter the name of a student: ").capitalize()

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} was not found")

# grades = {
#     "Ferda": "C",
#     "Burnell": "A",
#     "Zed": "B",
#     "Isabella": "A"
# }

# student = input("Enter the name of a student: ").capitalize()

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

# email = "danielbryan62f@gmail.com"

# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")


# List Comprehension
# List Comprehension = a concise way to create lists in python
#                    - Compact and easier to read than traditional loops
#                    - [Expression for value in iterable if condition]

# Traditional loop
# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)
# print(doubles)

# List Comprehension
# doubles = [x * 2 for x in range(1, 11)]
# print(doubles)

# triples = [y * 3 for y in range(1, 11)]
# print(triples)

# squares = [z * z for z in range(1, 11)]
# print(squares)

# fruits = ["apple", "orange", "coconut", "pineapple"]
# # fruits = [fruit.upper() for fruit in fruits]
# # fruit_chars = [fruit[0] for fruit in fruits]
# # print(fruit_chars)

# numbers = [1, 2, -3, 5, -1, -3, 4, -6, 19, 8, -7]
# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 == 1]
# print(positive_nums)
# print(negative_nums)
# print(even_nums)
# print(odd_nums)

# grades = [67, 90, 23, 56, 88, 81, 77, 71, 60, 59]
# passing_grades = [grade for grade in grades if grade >= 60]
# print(passing_grades)

# Match-case statements

# Match-case statements (Switch) = An alternative to using many 'elif' statements
#                                 Execute some code if a value matches a 'case'
#                                 Benefits: cleaner and syntax is more readable

# Traditional scenario
# def day_of_week(day):
#     if day == 1:
#         return "It is Sunday"
#     elif day == 2:
#         return "It is Monday"
#     elif day == 3:
#         return "It is Tuesday"
#     elif day == 4:
#         return "It is Wednesday"
#     elif day == 5:
#         return "It is Thursday"
#     elif day == 6:
#         return "It is Friday"
#     elif day == 7:
#         return "It is Saturday"
#     else:
#         return f"'{day}' is not a valid day"

# print(day_of_week(5))

# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is Sunday"
#         case 2:
#             return "It is Monday"
#         case 3:
#             return "It is Tuesday"
#         case 4:
#             return "It is Wednesday"
#         case 5:
#             return "It is Thursday"
#         case 6:
#             return "It is Friday"
#         case 7:
#             return "It is Saturday"
#         case _:
#             return f"'{day}' is not a valid day"

# print(day_of_week(7))

# def is_weekend(day):
#     match day:
#         case "Saturday" | "Sunday":
#             return True
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#             return False
#         case _:
#             return f"'{day}' is not a valid day"

# print(is_weekend("Friday"))


# String Methods  ------------------------------------------
# name = input("Enter your full name: ")
# name = "goat panda"
# name = "1232435"
# result = len(name) # Gives us length of a string
# result = name.find("p") # returns first occurrence of a character
# result = name.rfind("z") # returns last occurrence of a character: -1 means no results
# result = name.capitalize() # capitalizes the string
# result = name.upper() # makes all characters uppercase
# result = name.lower() # makes all characters lowercase
# result = name.isdigit() # returns a boolean if string contains ONLY digits
# result = name.isalpha() # returns a boolean if string contains ONLY alphabetical characters, space returns false since its not an aplahabet
# phone_number = "+254-124-456-213-10"

# result = phone_number.count("-") # returns an integer based on the number of counts of the character
# phone_number = phone_number.replace("-", " ") # returns a new string, replacing a character with another

# print(phone_number)
# print(help(str))


# Exercise Validate user input *** ---------------
# 1. username is no more than 12 characters
# 2. Username must not contain spaces
# 3. username must not contain digits

while True:
    username = input("Enter your username: ")

    if len(username) > 12:
        print("Username cannot be more than 12 characters")
        continue
    elif " " in username:
        print("Username cannot contain spaces")
        continue
    elif not username.isalpha():
        print("Username cannot contain numbers")
        continue
    else:
        print("Username entered successfully")
        break
