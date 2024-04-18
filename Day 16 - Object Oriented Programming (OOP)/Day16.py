#Object Oriented Programming (OOP)

class Dog: #class
  def __init__(self, name, age): #constructor
    self.name = name #attributes
    self.age = age #attributes
  def bark(self): #method
    print("Woof!") #it will print woof
  def get_name(self): #method
    return self.name #it retruns the name of the dog
  def get_age(self): #method
    return self.age #it returns the age of the dog
d = Dog("Tim", 34) #object
print(d.get_name()) #prints the name of the dog
print(d.get_age()) #prints the age of the dog
d.bark() #prints woof

"""OOPS is a programming paradigm that is used to create objects and classes. It is a way to structure and organize code to make it more readable, maintainable, and reusable.
"""
#Class is a blueprint for creating objects.
#Object is an instance of a class.

#Attributes are variables that are associated with an object.
#Methods are functions that belong to an object.
#Constructor is a special method that is called when an object is created. It is used to initialize the attributes of the object.

#Inheritance is a way of creating a new class based on an existing class.

# import another_module
# print(another_module.another_variable)

# import turtle
# timmy = turtle.Turtle()
# print(timmy)

from turtle import Turtle
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)

#Using OOPs concept creating car blureprint
class Car:
  def __init__(self, seats):
    self.seats = seats
my_car = Car(5)
print(my_car.seats)

#Object Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure and organize code
#car.stop() --> here car is an object and stop() is a method
#car = CarBlueprint() --> here car is an object and CarBlueprint() is a class
#car.speed --> here car is an object and speed is an attribute

my_screen = Screen() #my_screen is an object and Screen() is a class
print(my_screen.canvheight) #canvheight is an attribute
my_screen.exitonclick() #exitonclick() is a method

#https://docs.python.org/3/library/turtle.html
#https://cs111.wellesley.edu/reference/colors

#https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
#https://pypi.org/project/prettytable/
#https://pypi.org/
#https://pokemondb.net/pokedex/game/x-y

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Char" ])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

