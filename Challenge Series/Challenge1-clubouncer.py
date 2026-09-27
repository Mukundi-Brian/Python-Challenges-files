# Ask the user for their age then if 
# they are underage they can't enter the club, if the age is okay then welcome
# them to the club
age = 0
mistake_count = 0 # Add a mistake counter to prevent spamming

while True:
    try:
        age = int(input("What is your age? "))
        if 1 <= age <= 100:
            break
        mistake_count += 1
        print("That's not a valid age")
    except ValueError:
        print("What are you doing??? That's not a number!")
        mistake_count += 1

    if mistake_count == 3:
        print("Too many invalid attempts. Try again later")
        exit()

if age < 18:
    print("Go home kid!")
elif age >= 18:
    print("Welcome to the club!")