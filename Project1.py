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

def question_set(question,a,b,c,d,correct):
    print(question)
    print(a)
    print(b)
    print(c)
    print(d)
    user_answer = input("Enter your answer: ")
    if user_answer == correct:
        print("Correct! You get 1 Jolly Hotog!")
        return True
    else:
        print("You are wrong buddy, no Jolly Hotdog for you!\n"+"the correct answer is: " + correct) 
        return False

def track_score(score):
    score = 0 
    score += question_set("What is the capital of the Philippines?", "a. Manila", "b. Cebu", "c. Davao", "d. Quezon City","a")
    score += question_set("How many Islands are there in the Philippines?", "a. 6,942", "b. 1000", "c. 3", "d. 7,641","d")
    score += question_set("What is the most famous sport in the Philippines?", "a. Billiards", "b. Basketball", "c. Boxing", "d. Cockfighting","b")
    score += question_set("What is the national animal of the Philippines?", "a. Carabao", "b. Tarsier", "c. Dog", "d. Monkey","a")
    score += question_set("What is the national flower of the Philippines?", "a. Sampaguita", "b. Rose", "c. Sunflower", "d. Dandelion","a")
    return score

def final_score(score):
    print("Your final Jollyscore is: " + str(score))
    print("Thank you for playing the Jolly Quiz! " )

if __name__ == "__main__":
        welcome_message()
        user_score = track_score(0)
        final_score(user_score)