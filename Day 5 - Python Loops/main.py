# Loops - Loops are used to repeat the code again and again. Loops are used to execute a block of code repeatedly. 
# for loops - for loops are used to iterate over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# while loops - while loops are used to execute a block of statements repeatedly until a given condition is satisfied.
# do while loops - do while loops are used to execute a block of statements repeatedly until a given condition is satisfied.
# break - break statement is used to terminate the loop.
# continue - continue statement is used to skip the current iteration of the loop.
# nested loops - nested loops are loops inside loops.
# range() - range() function returns a sequence of numbers, starting from 0 by default, and increments by 1

#for loop syntax
#for item in list_of_items:
  #Do something to each item

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit,)
  print(fruit + " Pie")
print(fruits)

"""
#AVERAGE HEIGHT
You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

Example Input 1
156 178 165 171 187
In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

Example Output 1
total height = 857
number of students = 5
average height = 171
Example Input 2
151 145 179
Example Output 2
total height = 475
number of students = 3
average height = 158
"""

# Input a Python list of student heights
student_heights = input("Input a list of student heights").split() # split() function splits the string into a list
for n in range(0, len(student_heights)): # range() function returns a sequence of numbers, starting from 0 by default, and increments by 1
  student_heights[n] = int(student_heights[n])  # Convert each element to an integer
# Your code below this row 👇
total_height = 0 # Initialize a variable to store the total height
for height in student_heights: # Iterate over each height in the list
  total_height += height # Add the height to the total height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1 # Increment the number of students by 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students) # Calculate the average height 
print(f"average height = {average_height}")

#HIGH SCORE
"""
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x
Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91
"""

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Your code below this row 👇
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
    # print(highest_score)

print(f"The highest score in the class is: {highest_score}")

#RANGE
#for loops and ranges function
#syntax:
#for number in range(a,b):
#  print(number)

for number in range(1,10): #this for loop function range given as 1 to 10, but it will give between 1 to 9, so we need to add 1 in the end if we want to range 10.
  print(number)

for number in range(1,11,3): #here 3 is the step size, it will print 1,4,7,10.
  print(number)

total = 0
for number in range(1,101):
  total += number
print(total)
  
#ADDING EVEN NUMBERS
"""
You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

Example Input 1
10
Example Output 1
30
Example Input 2
52
Example Output 2
702
Hint
There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.
"""
target = int(input()) # Number between 0 and 1000
# Your code here 👇
even_sum = 0
for number in range(2, target + 1, 2):
  even_sum += number
print(even_sum)

# or

# alternative_sum = 0
# for number in range(1, target + 1):
#   if number % 2 == 0:
#     alternative_sum += number
# print(alternative_sum)

#FIZZBUZZ Game:
"""
You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

Your program should print each number from 1 to 100 in turn and include number 100.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

e.g. it might start off like this:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...etc

Hint
Remember your answer should start from 1 and go up to and including 100.

Each number/text should be printed on a separate line.
"""

target = 100
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

import random

#random(): Generates a random floating-point number between 0 and 1.
random_number = random.random()
print(random_number)
#randint(a, b): Generates a random integer between a and b (inclusive).
random_integer = random.randint(1, 100)
print(random_integer)
#choice(seq): Selects a random element from the given sequence seq.
my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print(random_element) 
#shuffle(seq): Randomly shuffles the elements of the given sequence seq in place.
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
#sample(population, k): Selects k unique random elements from the given population without replacement.
my_list = [1, 2, 3, 4, 5]
random_sample = random.sample(my_list, 3)
print(random_sample)

