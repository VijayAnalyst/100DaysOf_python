#Data Types

#String

print("Hello"[0])  #o/p: H

print("123" + "345")  #o/p: 123345

print("Hello" + "123")  #o/p: Hello123

#Integer

print(123 + 345)  #o/p: 468

#flot

3.14159

#Boolean

True
False

#Type Error, Type Checking and Type Conversion

len(4837)

#TypeError: object of type 'int' has no len()

num_char = len(input("What is your name?"))

#print("Youe name has " + num_char + " characters.")

#TypeError: can only concatenate str (not "int") to str

#Type Checking
type(num_char)

new_num_char = str(num_char)  #Type casting
type(new_num_char)  #Type Checking
print("Youe name has " + new_num_char + " characters.")

a = float(123)
print(type(a))  # <class 'float'>

print(70 + float("100.5"))  #170.5

print(str(70) + str(100))  #70100

#Adding two digits number
two_digit_number = input("Type a two digit number: ")

#print(type(two_digit_number)) #<class 'str'>
#Type casting
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two integers together
two_digit_number = first_digit + second_digit

print(two_digit_number)

#Mathematical Operations

3 + 5
7 - 4
3 * 2
print(6 / 3)  #o/p: 2.0
print(type(6 / 3))  #<class 'float'>
# ** - exponent
print(2**3)  #o/p: 8

#PEMDAS - LR
#Parentheses ()
#Exponents **
#Multiplication *
#Division /
#Addition +
#Subtraction -
#LR left to right

print(3 * 3 + 3 / 3 - 3)  # 9 + 1.0 - 3 => 10.0 - 3 => 7.0

print(3 * (3 + 3) / 3 - 3)  # 3 * 6 / 3 - 3 => 18 / 3 - 3 => 6 - 3 => 3
print(6 + 4 / 2 - (1 * 2))  # 6 + 2 - 2 => 8.0 - 2 => 6.0

a = int("5") / int(
    2.7
)  #int("5") is 5, int(2.7) is 2, so the code becomes: a = 5 ÷ 2 which equals 2.5, which is a float.

#BMI Calculator (Body Mass Index)

#BMI = weight(kg) / height^2(m^2)

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# Your code below this line 👇
weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float**2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)

#Number Manipulation and F Strings in Python
print(8 / 3)  # o/p: 2.6666666666666665

print(int(8 / 3))  # o/p: 2

print(round(8 / 3))  # o/p: 3

print(round(8 / 3, 2))  # o/p: 2.67

#Floor division
print(8 // 3)  # o/p: 2

print(type(4 / 2))  # <class 'float'>
print(4 / 2)  # o/p: 2.0
print(type(5 // 2))  # <class 'int'>
print(5 // 2)  # o/p: 2

# Reminder
print(type(5 % 2))  # <class 'int'>
print(5 % 2)  # o/p: 1

result = 4 / 2
result /= 2
print(result)

score = 0
#user score a point
score += 1
print(score)
print("your score is " + str(score))

#f-String
score = 0
height = 1.8
isWinning = True
print(
    f"your score is {score}, your height is {height}, you are winning is {isWinning}"
)

#Life in Weeks
age = input("What is your current age? ")
#Write your code below this line 👇
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"You have {weeks_remaining} weeks left.")
