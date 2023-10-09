# Project1.py
# Author: James Railey Cabrera


# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions

# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.

# Write a function that displays a welcome message to the user and explains the rules of the game

# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.
# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
# Score Tracking:

# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
# Function Utilization:

# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, and the correct answer, and return whether the user was correct.
# an example would be def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
# the return value should be a boolean (True or False) for whether the user was correct

# Create a function to display the final score, which takes the score as a parameter and displays a message.
# Loops:
# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d).

# Quiz game
# Write a function that displays a welcome message to the user and explains the rules of the game
def welcome_message():
    print("Welcome to Jolly Quiz!")
    print("Get the right answer and you get a Jolly Hotdog! ")
    print("Good luck! ( (´∀｀)つ―⊂ZZZ⊃ ")
    print ("")
    print ("")
    print ("")
welcome_message()
score = 0
# question 1
answer1 = input("What is the capital of the Philippines? \n a. Manila \n b. Cebu \n c. Davao \n d. Quezon City \n")
if input == "a":
    print("Correct! You get 1 Jolly Hotog!")
    score += 1
else: 
    print(str("Wrong! The correct answer is a. Manila"))
    score = 0

#question 2
answer2 = input("How many Islands are there in the Philippines? \n a. 6,942 \n b. 1000 \n c. 3 \n d. 7,641 \n")
if input == "d":
    print("Correct! You get 1 Jolly Hotog!")
    score = 1 + score
else: 
    print("Wow, ang galing! (wow, well done!) The correct answer is d. 7,641")
    score = 0
# question 3
answer3 = input("What is the most famous sport in the Philippines? \n a. Billiars \n b. Basketball \n c. Boxing \n d. Cockfighting \n")
if input == "b":
    print("Correct! You get 1 Jolly Hotog!") 
    score = 1 + score
else:
    
