"""
Importing Modules, Installing Packages, and Working with Aliases
"""
# import turtle
# tim = turtle.Turtle()

#from -- keyword
#turtle -- model name
#import -- keyword
#Turtle -- Thing in module

# from turtle import *

# from turtle import Turtle
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()

# Aliasing modules:
# from turtle import Turtle as t
# tim = t

# Installing Packages

# import heroes
# print(heroes.gen())

# import turtle as t
# tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
from turtle import Turtle, Screen
t = Turtle()

for _ in range(15):
    t.forward(10)
    t.color("white") #t.penup() 
    t.forward(10)
    t.color("black") #t.pendown()

screen = Screen()
screen.exitonclick()

########### Challenge 2 - Draw a Dashed Line ########








