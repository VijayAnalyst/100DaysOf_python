#1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")

#2. Ask the user for the city that they grew up in.
City_Name =input("What's the name of the city you grew up in?\n")

#3. Ask the user for the name of a pet.
Pet_Name =input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
#print("Your band name could be", City_Name + " " + Pet_Name, "\n")
#F-Strings:
#You can insert a variable into a string using f-strings.
#The syntax is simple, just insert the variable in-between a set of curly braces {}.
print(f"Your band name could be {City_Name} {Pet_Name}\n")
#5. Make sure the input cursor shows on a new line:

#Another way and Final code:
"""
print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)
"""
print("I hope! It's a nice name!")