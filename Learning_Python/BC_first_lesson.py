# Counter timer program, nested loops, lists, sets, tuples, dictionaries, Shopping cart program, 2d collections, quiz game, format specifiers

# Counter timer program
# import time

# # time.sleep(3)

# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}: {minutes:02}: {seconds:02}")
#     time.sleep(1)

# print("Wow! Time's up")

# Nested loops
# Nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:
# for x in range(1, 4):
#     for y in range(1, 10):
#         print(y, end=" ") 
#     print(f"{x} done")

# Print a rectangle chosen by the user specific width, height and symbol
# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbol = input("Enter the symbol you want to use (@, #, $, ...): ")

# for row in range(rows):
#     for column in range(columns):
#         print(symbol, end="")
#     print()

# Lists, sets, tuples, dictionaries
# Collection = single "variable" used to store multiple values
#   list = [] ordered and changeable, duplicates OK
#   set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   tuple = () ordered and unchangeable. Duplicates Ok. Faster

# fruits = ["apple", "orange", "banana", "coconut"]

# print(fruits[::-1])

# print(dir(fruits))
# print(help(fruits))

# Shopping list using the collections

# foods = []
# prices = []
# total = 0

# # while True:
# #     food = input("Enter a food to buy (q to quit):  ").strip()

# #     if food.lower() == "q":
# #         break
# #     else:
# #         price = float(input(f"Enter the price of a {food}: $"))
# #         foods.append(food)
# #         prices.append(price)

# print("----- Your Cart -----")
# prices = [12.24, 123.21, 109]
# prices = str(prices)

# number = 23
# new_number = str(number)
# for x in prices:
#     print(x)

# for food in foods:
#     print(food + "" + price)


# 2d = list is list in list

# fruits = ["apple", "banana", "orange", "watermelon"]
# vegetables = ["cabbage", "spinach", "tomato"]
# meats = ["chicken", "fish"]

# groceries = [fruits, vegetables, meats]

# # print(groceries[0][1])
# # print(groceries[2][1])
# # print(groceries)

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()

# Keypad exercise
# num_pad = ((1, 2, 3),
#            (4, 5, 6),
#            (7, 8, 9),
#            ("*", 0, "#"))

# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()


# Quiz Game

# questions = ("How many elements are in the periodic table?: ",
#              "Who is the strongest avenger?: ",
#              "Which animal lays the largest eggs?: ",
#              "Which planet is the hottest in the solar system?: ",
#              "What is glass made of?: ")

# options = (("A. 116 ", "B. 117", "C. 118", "D. 119"),
#            ("A. Thor", "B. Hulk", "C. Spider-man", "D. Dr.Strange"),
#            ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
#            ("A. Mars", "B. Pluto", "C. Earth", "D. Venus"),
#            ("A. Wood", "B. Sand", "C. Clay", "D. Plastic")
#            )

# answers = ("C", "A", "D", "D", "B")
# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("-----------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)

#     guess = input("Enter (A, B, C, D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print("Correct!")
#     else:
#         print("Wrong!")
#         print(f"The correct answer is: {answers[question_num]}")
#     question_num += 1

# print("-----------------------")
# print("--------RESULTS--------")
# print("-----------------------")

# print("Answers: ", end="")
# for answer in answers:
#     print(answer, end="")
# print()

# print("Guesses: ", end="")
# for guess in guesses:
#     print(guess, end="")
# print()

# score = int(score / len(questions) * 100)
# print(f"Your score is: {score}%")

# Format Specifiers
# Format specifiers = (:flags) format a value based on what flags are inserted

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive values
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
