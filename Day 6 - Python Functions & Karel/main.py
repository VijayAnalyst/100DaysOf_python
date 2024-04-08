#Python Functions & Karel

print("Hello")
num_char = len("Hello") 
print(num_char)

def my_function(): #defining a function
  print("Hello") #do this
  print("Bye") #then do this
  print("see you next time champ!") #finally do this

my_function() #calling a function

#while loop
number = 6 #number of hurdles
while number > 0: #while number of hurdles is greater than 0
  print("hello")
  number -= 1 #decrease number of hurdles by 1
  print(number)


"""
The while Loop:
With the while loop we can execute a set of statements as long as a condition is true.
"""

#Example:
#Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1

#Note: remember to increment i, or else the loop will continue forever.

"""
The break Statement:
With the break statement we can stop the loop even if the while condition is true.
"""

#Example
#Exit the loop when i is 3:

i = 1
while i < 6:
  print(i) #print i: 1,2,3
  if i == 3:
    break #stops the loop
  i += 1 

"""
The continue Statement:
With the continue statement we can stop the current iteration, and continue with the next.
"""

#Example:
#Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3: 
    continue #skips the rest of the code and goes back to the top
  print(i) #prints the number: 1, 2, 4, 5, 6


"""
The else Statement
With the else statement we can run a block of code once when the condition no longer is true.
"""
#Example
#Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

"""
For Loops:
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

#Example
#Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#The for loop does not require an indexing variable to set beforehand.

"""
Looping Through a String:
Even strings are iterable objects, they contain a sequence of characters:
"""

for x in "banana":
  print(x)


"""
The break Statement:
With the break statement we can stop the loop before it has looped through all the items:
"""

#Example
#Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Example
#Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

"""
The continue Statement:
With the continue statement we can stop the current iteration of the loop, and continue with the next:
"""
#Example
#Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

"""
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
"""

#Example
#Using the range() function:

for x in range(6):
  print(x)

#Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

"""
The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6)
"""

#Example
#Using the start parameter:

for x in range(2, 6):
  print(x)