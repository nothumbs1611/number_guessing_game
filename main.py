#Number Guessing Game Objectives:
from art import logo
import random

#player selects a difficulty level:
easy = 10
hard = 5

def difficulty():
    level = input("chose a difficulty.  Type 'easy' or 'hard'\n").lower()
    if level =="easy":
        return easy
    else:
        return hard


# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
def check_answer(guess, number, attempts):
    if guess > number:
        print(" too high.\n")
        return attempts -1
    elif guess < number:
        print("too low.\n")
        return attempts -1
    else:
        print(f"You guessed the correct number!")
# If they got the answer correct, show the actual answer to the player.

# Track the number of turns remaining.
def game():
    # Include an ASCII art logo.
    print(logo)
    print("Welcome to the number guessing game\n")
    # program randomly selects a number between 1-100:
    print("I'm thinking of a number between 1 and 100, try to guess what it is.\n")
    number=random.randint(1,100)
    #print(f"true number is: ",number)

    attempts = difficulty()
    guess = 0
    while guess != number:
        print(f"you have {attempts} turns remaining to guess the correct number\n")
        # Allow the player to submit a guess for a number between 1 and 100.
        guess = int(input("Guess a number between 1 and 100: "))

        #track the number of turns and reduce by 1 if they get it wrong:
        attempts = check_answer(guess, number, attempts)
        if attempts ==0:
            print("you have run out of guesses, you lose")
            return
        elif guess != number:
            print("try again\n")

# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
game()

