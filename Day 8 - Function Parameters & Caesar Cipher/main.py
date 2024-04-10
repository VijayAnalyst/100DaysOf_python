#Function Parameters & Caesar Cipher

# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

#Functions
def greet():
  print("Hello")
  print("How do you do?")
  print("Isn't the weather nice today?","\n")

greet()

#Functions with input
def greet_with_name(name):  #name is the parameter
  print("Hello " + name)
  print("How do you do? " + name)
  print(f"Isn't the weather nice today? {name} \n")

greet_with_name("Angela") #Angela is the argument

#Functions with more than 1 input

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")  

#Functions with funtion parameters
greet_with("Angela", "London")
#vs
greet_with("Vijay", "Washington D.C.")

#Functions with keyword arguments
greet_with(location = "London", name = "Angela")

"""
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 * 4) / 5
               = 1.6
But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

Example Input
3
9
Example Output
You'll need 6 cans of paint.
Hint
"""
import math #importing math module

def paint_calc(height, width, cover): #height, width, cover are the parameters
  num_cans = (height * width) / cover
  round_up_cans = math.ceil(num_cans) #math.ceil() rounds up the number
  print(f"You'll need {round_up_cans} cans of paint.")

# Your code above this line 👆
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)#test_h, test_w, coverage are the arguments

"""
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.


Here are the numbers up to 100, prime numbers are highlighted in yellow:


Example Input 1
73
Example Output 1
It's a prime number.
Example Input 2
75
Example Output 2
It's not a prime number.
"""
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

# Your code above this line 👆
n = int(input()) # Check this number
prime_checker(number=n)
