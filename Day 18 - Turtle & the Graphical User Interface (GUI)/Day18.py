from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

def turtle_moving_instruction():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
turtle_moving_instruction()

screen = Screen()
screen.exitonclick()


#Day 18:
#Turtle and tuples and importing modules
#Turtle is a module in python which is used to create different shapes and designs.
#Turtle is a library which is imported using import keyword.
#Turtle is a function which is used to create a turtle.
#Turtle is a class which is used to create different shapes and designs.

# https://docs.python.org/3/library/turtle.html
# https://trinket.io/docs/colors
# https://cs111.wellesley.edu/reference/colors

# Understanding Turtle Graphics and How to use the Documentation

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)

screen = Screen()
screen.exitonclick()

#GUI - Graphical User Interface
#GUI is a way to interact with the computer using a graphical user interface.
#Tuples
#Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.
#Example:
# tuple1 = (1,2,2,3,5,4,6)
# tuple2 = ("Red", "Green", "Blue")
# print(tuple1)
# print(tuple2)

# details = ("Abhijeet", 18, "FYBScIT", 9.8)
# print(details)

# #Tuples Indexes
# #Tuples are indexed just like lists.
# #Positive Indexing:
# #As we have seen that we can access items using its index with the help of square bracket [].
# #Negative Indexing:
# #Similar to list, tuples also support negative indexing.
# #Example:
# countries = ("Spain", "Italy", "India", "England", "Germany")
# #            [0]      [1]      [2]       [3]        [4]  
# print(countries[0])
# print(countries[1])
# print(countries[2])
# print(countries[3])
# print(countries[4])

#Generate Random RGB Colours
#Python Tuples :
#Example: (1,3,8) 

my_tuple = (1,3,8) #tuple
print(my_tuple) #(1,3,8)
my_tuple[2] #8

my_tuple[2] = 12 #TypeError: 'tuple' object does not support item assignment

#Tuples is immutable, We cannot change the value of tuple once it is created.
#then why we need tuples?
#Answer: Tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, we will see how to use tuple later.

list(my_tuple) #chaning tuple to list

#python List;
#Example: [1,3,8]

#https://www.w3schools.com/colors/colors_rgb.asp
import random
def random_color():#function
  r = random.randint(0,255) #random integer
  g = random.randint(0,255)
  b = random.randint(0,255)

  random_color = (r,g,b) #tuple
  return random_color