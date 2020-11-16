import requests
import random
import time
import urllib

# Set variables
questionurl = "https://opentdb.com/api.php?amount=10&type=multiple&encode=url3986"
score = 0
question_number = 0

# Get Questions
r = requests.get(questionurl)
questions = r.json()

# Start the quiz
for question in questions["results"]:  # Process the questions
    user_answer = 0
    valid_answer = False
    question_number += 1

    question_text = question["question"]
    question_text = urllib.parse.unquote(
        question_text)  # Convert text from URL encoding
    correct_answer = question["correct_answer"]
    correct_answer = urllib.parse.unquote(correct_answer)
    answers = [question["correct_answer"], question["incorrect_answers"][0],
               question["incorrect_answers"][1], question["incorrect_answers"][2]]

    for x in range(0, 4):
        # Convert Questions from URL Encoding
        answers[x] = urllib.parse.unquote(answers[x])

    # Ask the question
    print("\nQuestion " + str(question_number) + ": " + question_text)

    answers = random.sample(answers, k=4)  # randomise answers
    x = 0

    for answer in answers:  # Print the answers on screen
        x += 1
        print(str(x) + ": " + answer)

    while valid_answer == False:  # Await the users answer
        user_answer = int(input("\nChoose answer: "))
        if user_answer == 1 or user_answer == 2 or user_answer == 3 or user_answer == 4:
            valid_answer = True

    user_answer_text = answers[user_answer - 1]

    # Check the answer

    if user_answer_text == correct_answer:
        print("\nCorrect!!!!!!!!!")
        score += 1
    else:
        print("\nWrong! :( :(")
        print("You answered: " + user_answer_text +
              ". The correct answer was " + correct_answer)

    time.sleep(1)

# End the game

print("Your score was " + str(score))
if score >= 8:
    print("Excellent job!")
elif score > 4 and score < 8:
    print("Middle of the road")
else:
    print("Come on... that's not good")
