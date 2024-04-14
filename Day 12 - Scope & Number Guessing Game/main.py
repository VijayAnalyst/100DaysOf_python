################### Scope ####################

enemies_1 = 1 #global variable

def increase_enemies():
  enemies_2 = 2 #local variable
  print(f"enemies inside function: {enemies_2}")

increase_enemies()
print(f"enemies outside function: {enemies_1}")

game_level = 3
def create_enemy():
  enemies_list = ["Skeleton", "Zombie", "Alien"]
  if game_level < 5:
    new_enemy = enemies_list[0]
  print(new_enemy)

create_enemy()

#how to modify global variable
#Version1 
i_number = 1
def increase_number():
  global i_number
  i_number += 1
  print(i_number)

increase_number()
#print(i_number)

#Version2
D_number = 10
def decrease_number():
  print(f"D_number inside function: {D_number}")
  return D_number - 1

D_number = decrease_number()
print(f"D_number outside function: {D_number}")

#Global constants
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@THE_VYK"

#Python there is no block scope
#Inside a if/else/for/while code block is the same as outside it.
def bar():
    my_variable = 9 

    if 16 > 9:
      my_variable = 16

    print(my_variable) # Prints 16

bar()
