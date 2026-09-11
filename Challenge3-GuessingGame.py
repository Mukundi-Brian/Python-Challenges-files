# #This code is a guessing game where the computer picks a number and 
# #the user has to guess the number and everytime they get it wrong 
# #the computer says either higher or lower

import random

# computer_choice = random.randint(1, 10)
# user_choice = None

# while user_choice != computer_choice:
#     user_choice = int(input("Guess the number between (1-10): "))
#     if user_choice not in range(1,11):
#         print("You lose for not following instructions!!!")
#         break
#     elif user_choice < computer_choice:
#         print("Guess Higher!!")
#     elif user_choice > computer_choice:
#         print("Guess Lower!!")
    
    
# if user_choice == computer_choice:
#     print("Excellent Work!! You got it")

# Challenge 3.1 same guessing game but this 
# time there are a limited number of turns

computer_choice = random.randint(1,20)
user_choice = 0
i = 0
mistake_count = 0

for i in range (5):
    while True:
        try:
            user_choice = int(input("Guess the number (1-20): "))
            break
        except ValueError:
            print("What are you doing??? You have lost a turn")
            mistake_count += 1
            if mistake_count == 3:
                print("Three Strikes. Look what you've done!!!")
                break
    if mistake_count == 3:
        break
    if user_choice > 20:
            print("You lose for not following instructions!!!")
            break
    elif user_choice == computer_choice:
        print("Excellent work!!! You got it.")
        break
    if i == 4:
        print("Attempts over you lose!!!")
    elif user_choice < computer_choice:
        # print("Guess Higher! You have " + str(4-i) + " attempt(s) Remaining!!!")
        print(f"Guess Higher! You have {4-i} Attempt(s) Remaining.")
    elif user_choice > computer_choice:
        # print("Guess Lower! You have " + str(4-i) + " attempt(s) remaining")
        print(f"Guess Lower! You have {4-i} Attempt(s) remaining.")

# Things to note: Use formatted strings, for loops are iterated automatically on python, try and except
    
    