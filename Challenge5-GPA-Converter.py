# This code converts your average scores into GPA (Grade Point Average)
#The program should:
# 1. Ask the user for their scores across multiple subjects
# 2. Calculate the average score of the subjects
# 3. Divide the average across the subjects to get the GPA
# 4. Compare the GPA across the predefined ones and give a grade

# A. Let's try implementing it using a for loop
# The core idea is:
# 1. Ask the user the number of subjects
# 2. Based on the number of subjects run the for loop
# 3. Store the scores in an empty list
# 4. Once the for loop is done we use that data to calculate GPA

# B. Let's add the user checks to prevent misuse and crashing the code
# The core idea is:
# 1. Prevent value errors
# 2. Prevent unreasonable input like more than 50 subjects or negative scores
# 3. Prevent spamming wrong inputs

# Let's import statistics to calculate average
import statistics

Gpa_a = "A (4.0)"
Gpa_b = "B (3.0)"
Gpa_c = "C (2.0)"
Gpa_d = "D (1.0)"
Gpa_f = "F (0.0)"

scores = [] # Empty list waiting for scores
user_no_of_subjects = 0 # The code complains without these because of the try block
user_scores = 0
mistake_count = 0
user_average = 0

print("Hello, Let's calculate your GPA! :) \n") # Welcome Greeting

while True: # Looping to ensure that a mistake does not terminate the program
    try: 
        user_no_of_subjects = int(input("How many sujects do you do?: "))
        if 1 <= user_no_of_subjects <= 100:
            break
        mistake_count += 1
        print("Subjects must be between (1-100)")
    except ValueError:
        mistake_count += 1
        print("Enter a valid value.")
    if mistake_count == 5:
        print("Too many invalid attempts. Try again some other time. Exiting Program.\n")
        exit()

mistake_count = 0 # Let's reset the mistake counter before they start entering scores

# Let's implement a for loop based on the users' number of subjects
for i in range(user_no_of_subjects):
    while True:
        try:
            user_scores = float(input(f"Enter your scores for subject {i + 1}: "))
            if 0 <= user_scores <= 100: # Wow this code checks if the user entered a value between 0-100 if not it will loop infinitely until mistake count == 3
                scores.append(user_scores)
                break
            mistake_count += 1
            print("Score must be between (0 - 100)")

        except ValueError:
            mistake_count += 1 # Increasing mistake counter to catch spamming
            print("Invalid response! Try again.")

        if mistake_count == 10: # Terminating the program after a certain amount of invalid responses
            print("Too many invalid attempts. Try again later.")
            exit()
            
# # If user enters nothing exit the program
# if not scores:
#     print("You did not enter a value. Exiting Program \n")
#     exit()

try:
    user_average = statistics.mean(scores) # Average score of the user
except ZeroDivisionError:
    print("Cannot divide by zero")

print("Awesome! Let's do some math :) \n") # A message just because

# The classifications for GPAs calculations
if user_average >= 70:
    print(f"Your GPA is {Gpa_a} \n")
elif user_average >= 60:
    print(f"Your GPA is {Gpa_b} \n")
elif user_average >= 50:
    print(f"Your GPA is {Gpa_c} \n")
elif user_average >= 40:
    print(f"Your GPA is {Gpa_d} \n")
else:
    print(f"Your GPA is {Gpa_f} \n")

# What I learnt:
# 1. Using while loops in reverse, instead of breaking if wrong, break if right
# 2. If not and try blocks to catch errors
# 3. Implementing choices between values mostly for floats because in range wont work
# 4. Trying and failing is the idea and part of the process
# 5. Don't obsess over perfection
# 6. Start simple then iterate and document code for yourself as well as others