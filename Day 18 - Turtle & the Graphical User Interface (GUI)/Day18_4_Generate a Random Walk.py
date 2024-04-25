# https://en.wikipedia.org/wiki/Random_walk
# https://docs.python.org/3/library/turtle.html

# from turtle import Turtle, Screen
# import random 

#https://www.w3schools.com/colors/colors_rgb.asp

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    random_color = (r,g,b)
    return random_color

########### Challenge 4 - Random Walk ########
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270]

# for _ in directions:
#     tim.forward(30)
tim.pensize(10)
tim.speed("fastest")

for _ in range(200):
    #tim.color(random.choice(colours))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
