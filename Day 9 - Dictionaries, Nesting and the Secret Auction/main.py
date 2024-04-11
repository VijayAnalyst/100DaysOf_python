#Dictionary : {key:value} 
#Dictionary is a collection of key value pairs
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."
} #Defining a dictionary
print(programming_dictionary["Function"]) #prints the value of the key Function
#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)
#Create an empty dictionary
empty_dictionary = {}
#Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)
#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)
#Loop through a dictionary
for key in programming_dictionary: #prints the key
  print(key)
  print(programming_dictionary[key]) #prints the value of the key

# GRADING PROGRAM
"""
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.

The final version of the student_grades dictionary will be checked.

DO NOT modify lines 1-7 to change the existing student_scores dictionary.

DO NOT write any print statements.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"

Expected Output
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
Hint
Remember that looping through a Dictionary will only give you the keys and not the values.

If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values.

At the end of your program, the print statement will show the final student_scores dictionary, do not change this.
"""

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Covert scores into grades.
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

print(student_grades)

#nesting
#nesting a list in a dictionary
#Normal dictinory: {key:value}
Normal_dictionary = {
  "key1" : "value1",
  "key2" : "value2"
}
#Nesting a list in a dictionary
# {key: [list]}
# {key: [list1, list2, list3]}
List_dictinory ={
  "key01" : "[List1,List2,List3]"
}
travel_log = {
  "France" : ["Paris", "Lille", "Dijon"],
  "Germany" : ["Berlin", "Hamburg", "Stuttgart"]
}
#Nesting a dictionary in a dictionary
dictionary_in_dictionary = {
  "key001" : {
    "key0001" : "value1",
    "key0002" : "value2"
  }
}

travel_log2 = {
  "France" : {
    "cities_visited" : ["Paris", "Lille", "Dijon"],
    "total_visits" : 12
  },
  "Germany" : {
    "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits" : 5
  }
}

#Nesting a dictionary in a list
travel_log3 = [
  {
    "country" : "France", 
    "cities_visited" : ["Paris", "Lille", "Dijon"],       
    "total_visits" : 12
  },
  {
    "country" : "Germany", 
    "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits" : 5
  }
]

first_country = travel_log3[0] #prints the first dictionary in the list
print(first_country) 

print(first_country["country"])

#DICTIONARY IN LIST
"""
You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries. Your job is to create a function that can add new countries to this list.

Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the travel_log.

add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
DO NOT modify the travel_log directly. The goal is to create a function that modifies it.

Example Input
Brazil
5
["Sao Paulo", "Rio de Janeiro"]
Example Output
I've been to Brazil 5 times.
My favourite city was Sao Paulo.
Hint
Look at the function call above to see what the name of the function should be.

The inputs for the function are positional arguments. The order is very important.

Feel free to choose your own parameter names.
"""

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Your code here 👇
def add_new_country(name, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")


