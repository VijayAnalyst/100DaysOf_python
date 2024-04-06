#Day 4 - Randomisation and Python Lists
#module means a piece of code that is responsible for a specific task
import my_module
print(my_module.PI)
#random is a module
import random
random_integer = random.randint(1, 10)
print(random_integer)
#random float between 0 and 1
#it gives 0.0000 - 0.9999....
random_float = random.random()
print(random_float)
#Decimal numbers between 0 and 5
random_float = random.random() * 5
print(random_float)
#love score using random module 
LoveScore = random.randint(1,100)
print(f"Your love score is {LoveScore}")

#HEADS OR TAILS

"""You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. "Heads", not "heads".

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".

e.g. 1 means Heads 0 means Tails

Example Output
Heads
or

Tails"""

import random
random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")

#LISTS
#Lists means a data structure, it is a way of organising and storing data in python.
#It is a way of storing grouped pieces of data.
#list = [item1, item2]
fruits = ["Cherry", "Apple", "Pear"]
#In python, the order of the data is determined by the order in the list. its called the offset or the index.
#The offset or the index starts from 0.
#So the first item in the list is the offset or the index 0 and secon item is the offset or the index 1 and so on.
#The offset or the index of the last item in the list is the len(list) - 1. 
print(fruits)

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connect"]
print(states_of_america[1])
print(states_of_america[-1]) #The last item in the list
#You can change the item in the list by using the offset or the index.
states_of_america[1] = "Pencilvania"
print(states_of_america)
print(states_of_america[1])
#You can add an item to the list by using the append function.
states_of_america.append("Angelaland")
print(states_of_america)
#You can add a list to the list by using the extend function.
states_of_america.extend(["Angelaland", "Jack Bauer Land"])
print(states_of_america)
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connect", "Angelaland", "Jack Bauer Land"]
num_of_states = len(states_of_america) #The number of items in the list, the len function is used to calculate the number of items in the list.
print(states_of_america[num_of_states - 1])

#BANKER ROULETTE
"""You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 1 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

NOTE: Don't worry about getting hold of the input(), we've done the work behind the scenes to import everything.

HINT: Assume that names looks like this: input: x, y, z, names = ["x", "y", "z"]

Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!"""

import random
# Split the input string into a list of names
#names_string = input("Give me everybody's names, separated by a comma. ")
#names = names_string.split(", ")
names_list = "Alice, Bob, Charlie, David, Emily"
names = names_list.split(", ")

# Get the total number of names
total_names = len(names)
# Generate a random index within the range of the list
random_index = random.randint(0, total_names - 1)
# Select the name at the random index
random_name = names[random_index]
# Print the selected name
print(f"{random_name} is going to buy the meal today!")

#-----------

#Nested Lists
#A list within a list

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegtables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegtables]

print(dirty_dozen)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons" #Change the item in the list, it means replace the item in the list.
fruits.append("Lemons") #Add a new item to the end of the list.
print(fruits)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1]) #The first [1] means the second list in the nested list, the second [1] means the second item in the second list.
#First, try printing out:
print(dirty_dozen) 
#Then print out:
print(dirty_dozen[0]) #The [0] means the first list in the nested list.
print(dirty_dozen[1]) #The [1] means the second list in the nested list.
print(dirty_dozen[1][2]) #The frist [1] means the second list in the nested list, the second [2] means the third item in the second list.
print(dirty_dozen[1][3]) #The frist [1] means the second list in the nested list, the second [3] means the fourth item in the second list.

#TREASURE MAP
"""
You are going to write a program that will mark a spot on a map with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']
Now it looks a bit more like the coordinates of a real map:


Your job is to write a program that allows you to mark a square on the map using a letter-number system.


So an input of A3 should place an X at the position shown below:


First, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
Example Input 1
B3
Example Output 1
Hiding your treasure! X marks the spot.
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']
Example Input 2
B1
Example Output 2
Hiding your treasure! X marks the spot.
['⬜️', 'X', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', '⬜️️', '⬜️️']
Hints
See if this List method helps you: https://www.w3schools.com/python/ref_list_index.asp

Remember that nested Lists in Python are accessed from outside to inside. e.g. In the List below:

list = [['A', 'B, 'C'], 'E', 'F', 'G']
E is list[1] C is list[0][2]

Check your formatting. This is correctly formatted:
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
vs.

Incorrectly formatted (missing a space before 'X and extra space after the X and extra space before the comma):

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️','X ' , '⬜️']
"""
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ")
#position = input() # Where do you want to put the treasure?
# Your code below
letter = position[0].lower() #taking the first letter of the input and converting it to lower case.
abc = ["a", "b", "c"] #creating a list of letters.
letter_index = abc.index(letter) #finding the index of the letter in the list.
number_index = int(position[1]) - 1 #finding the index of the number in the list. -1 because the index starts from 0. 
map[number_index][letter_index] = "X" #replacing the item in the list.

print(f"{line1}\n{line2}\n{line3}") #printing the list. \n means new line. f means format string.