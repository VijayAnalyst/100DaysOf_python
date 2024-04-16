import random

from art import logo, vs
from game_data import data

#from replit import clear
# print(logo)
score = 0
Start_Game = True
while Start_Game:
    # clear()
    #print(logo)
  compare_A = random.choice(data)
  compare_B = random.choice(data)

  print(f"Compare A : {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}")
  print(vs)
  print(f"Compare B : {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}")
  User_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

  
  if User_answer == 'a':
    if compare_A['follower_count'] > compare_B['follower_count']:
      score += 1
      print(f"You are right! Current score : {score}")
    else:
      print(f"Sorrry, that's wrong. Final score : {score}")
      Start_Game = False
  elif User_answer == 'b':
    if compare_B['follower_count'] > compare_A['follower_count']:
      score += 1
      print(f"You are right! Current score : {score}")
    else:
      print(f"Sorrry, that's wrong. Final score : {score}")
      Start_Game = False



