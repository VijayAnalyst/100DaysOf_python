#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

random_number  = random.choice(range(1,101))

def hard():
  attempts = 5

  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))  
    if guess == random_number:
      print(f"You got it! The answer was {random_number}.")
      break
    elif guess > random_number:
      print("Too high.")
      attempts -= 1  
    elif guess < random_number:
      print("Too low.")
      attempts -= 1
    if attempts == 0:
      print("You've run out of guesses, you lose.")
      print(f"Pssst, the correct answer is {random_number}")
      break

def easy():
  attempts = 10

  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))  
    if guess == random_number:
      print(f"You got it! The answer was {random_number}.")
      break
    elif guess > random_number:
      print("Too high.")
      attempts -= 1  
    elif guess < random_number:
      print("Too low.")
      attempts -= 1
    if attempts == 0:
      print("You've run out of guesses, you lose.")
      print(f"Pssst, the correct answer is {random_number}")
      break


def number_guessing_game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  #print(f"Pssst, the correct answer is {random_number}")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == "easy":
    easy()
  elif difficulty == "hard":
    hard()
  else:
    print("Invalid input.")

number_guessing_game()