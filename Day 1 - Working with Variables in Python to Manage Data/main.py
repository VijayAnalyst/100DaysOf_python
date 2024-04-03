# Write your code below this line 👇

print("Hello World! \n")
print ("Hello" + " " + "Angela \n")

#Write your code for printing the output as given below 
#She said: "Hello" and then left.
print("She said: \"Hello\" and then left.")
print('She said: "Hello" and then left.\n')

print("A 'single quote' inside a double quote")
print('A "double quote" inside a single quote')
print("Alternatively you can just \"escape\" the quote\n")

print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.\n")

#Multiply argument a with argument b and return the result:
#input function
#print(input("What is your name? ")) #❌
#print(input()) #✅

num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
print(num1 * num2, "\n")

#lambda arguments : expression
x = lambda a, b : a * b
print(x(5, 6),"\n")

#The len() function is used to return an integer value which indicates the number of items in an object
#print(len(input()))
numOfLetters = len("Angela")
print(numOfLetters, "\n")

#This program takes two inputs. The first input is stored in a variable called a. The second input is stored in a variable called b.
#Write a program that switches the values stored in the variables a and b.
# There are two variables, a and b from input
a = input("Enter a number: ") #print(input())
b = input("Enter a number: ") #print(input()) 
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇

temp = a
a = b
b= temp

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)