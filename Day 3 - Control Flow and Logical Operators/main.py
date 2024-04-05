# Day 3 - Beginner - Control Flow and Logical Operators
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You are eligible to ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride. See you again!")
#Syntax - Control Flow with if/else and Conditional Operators
# if condition:
#   do this
# else:
#   do this
#Here indentations are very important. need to be very careful with indentations.

#if you meshup indentations with the code, it will give you an indentation error.
#IndentationError: unexpected indent or expected an indented block

#Comparison Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to
#Modulo Operation
# % - gives you the remainder of a division
# 7 % 2 = 1
# 7 % 3 = 1

#remember python is case sensitive.

#Write a program that works out whether if a given number is an odd or even number.

number =int(input("Enter a number: "))
#Even numbers can be divided by 2 with no remainder.
if number % 2 == 0:
  print("This is an even number.")
# Otherwise (number cannot be divided by 2 with 0 remainder).
else:
  print("This is an odd number.")

#Nested if/else - syntax
#if condition:
#  if another condition:
#    do this
#  else:
#    do this
#else:
#  do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You are eligible to ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride. See you again!")

#if/elif/else - syntax
#if condition1:
#  do A
#elif condition2:
#  do B
#else:
#  do this
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You are eligible to ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride. See you again!")
  
'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Equal to or over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.
'''

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#height = float(input())  # in meters e.g., 1.55
#weight = int(input())  # in kilograms e.g., 72
# Your code below this line 👇
bmi = weight / (height * height) #bmi = weight / (height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

#LEAP YEAR
# Which year do you want to check?
year = int(input("Which year do you want to check? "))
#year = int(input())
"""This is how you work out whether if a particular year is a leap year.
- on every year that is divisible by 4 with no remainder
- except every year that is evenly divisible by 100 with no remainder
- unless the year is also divisible by 400 with no remainder"""

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

#Logical Operators
# and - both conditions have to be true  ex., A and B
# or - either one of the conditions have to be true ex., A or B
# not - reverses a condition ex., not A



