#Normal Functions:
#def my_functions():
  #do this
  #then do this
  #finally do this

#Functions with inputs
#def my_function1(something):
  #do this with something
  #then do this
  #finally do this  
#something()

#Functions with outputs
def my_function():
  result = 3 * 2
  return result

print(my_function())

#Add two paraemters like full name
def format_name(f_name, l_name): #f_name and l_name are parameters
  result = f_name.title() + " " + l_name.title() #result is the output. title() is a function, it will return the title case version of the string which means first letter is capital and the rest are small. concactenation is done with + sign. " " is used to add space between the two strings"
  return result #return is the end of the function, it will replace the function call with the output. 

f_name = input("What is your first name? ") #input is a function, it will return the user input.
l_name = input("What is your last name? ")
print(format_name(f_name, l_name)) #function call

#multiple return values
def format_name(f_name, l_name): #f_name and l_name are parameters
  if f_name == "" or l_name == "": #if the user does not provide any input, the function will end 
    return "You didn't provide valid inputs." #return is the end of the function, it will replace the function call with the output.
  result = f_name.title() + " " + l_name.title() #result is the output. title() is a function, it will return the title case version of the string which means first
  return result #return is the end of the function, it will replace the function call with the output.

f_name = input("What is your first name? ")
l_name = input("What is your last name? ")
print(format_name(f_name, l_name)) #function call 

#DAYS IN MONTH
"""
Instructions
Convert the is_leap() functtion
In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

Create a new function called days_in_month()
You are then going to modify a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)
And it will use this information to work out if the year is a leap year and decide the number of days in the month, then return that as the output, e.g.:

28
The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

Hint
Look at the function call at the bottom of the code to see the positional arguments. The order is very important.

Feel free to choose your own parameter names.

Remember that month_days is a List and Lists in Python start at position 0. So the number of days in January is month_days[0]

Be careful with indentation.
"""
def is_leap(year): #year is the parameter
  if year % 4 == 0: #if the year is divisible by 4
    if year % 100 == 0: #if the year is divisible by 100
      if year % 400 == 0: #if the year is divisible by 400
        return True #it is a leap year
      else: #if the year is not divisible by 400 
        return False #it is not a leap year
    else: #if the year is not divisible by 100
      return True #it is a leap year
  else: #if the year is not divisible by 4
    return False #it is not a leap year

def days_in_month(year, month): #year and month are the parameters
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #the number of days in each month
  if month == 2 and is_leap(year): #if the month is February and the year is a leap year
    return 29 #it has 29 days
  else: #if the month is not February or the year is not a leap year
    return month_days[month - 1] #it has the number of days in the month
# Your code above 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month) #days is the output
print(days)

#Docstrings :- Docstrings are used to document the functions, classes, modules, and methods.
#Docstrings are written as comments immediately after the definition of the function, class, module, or method.
#Docstrings are not ignored by Python, but they are read by Python and used by documentation generators.
#Docstrings are used to provide a detailed description of the function, class, module, or method.
#Docstrings are written in reStructuredText format and use triple quotes (""") to enclose the doc


#while loop
#Seeting a flag before the loop like game_is_on = True
#while something_is_true:
  #do this
#removing the flag like game_is_on = False

#recursion means calling a function, a defined function can call itself.
#recursion is a way of solving a problem by breaking it down into smaller subproblems, and then solving those subproblems recursively.
#recursion is used when a function calls itself.