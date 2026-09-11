# Hello, this code is supposed to be a text quiz game
# It should do the following:
# 1. Store general knowledge question and answers
# 2. Ask the user a series of general knowledge questions
# 3. The questions should loop and update the scores
# 3. Score the users based on the number of correct answers
# 4. Print user's score and different messages based on performance

user_score = 0 # Initial User Score

quiz_questions = {
    "What is the capital of France?" : "Paris",
    "What is the chemical symbol for the element Gold?": "AU",
    "In what year did the RMS Titanic Sink?": "1912",
    "Which planet in our solar system is considered the 'red planet'?": "Mars",
    "Which superhero uses webs as one of their primary weapons?": "Spiderman"
}

for question,correct_answer in quiz_questions.items():
    user_answer = input(f"Question: {question}: ").strip().lower()
    if user_answer == correct_answer.strip().lower():
        print("Nice you got it!")
        user_score += 1

    elif user_answer == "":
            print("You didn't write anything, thats a 0")

    else:
        print(f"Ouf! You missed it. The correct answer is '{correct_answer}'")

# Print different messages based on the user's scores
if 0 <= user_score <= 2:
    print(f"Your score is {user_score}. You need to do more research!")
elif user_score == 3:
    print(f"Your score is {user_score}. Not bad but not good either!")
elif user_score > 3:
    print(f"Your score is {user_score}. You are a seasoned Veteran! Good job.") 