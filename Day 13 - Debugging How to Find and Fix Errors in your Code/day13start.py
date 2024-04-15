############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): #range is not inclusive of the last number, so it will never reach 20
#     if i == 20: #range does not include 20, so i will never equal 20
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"] #list starts at 0, so the last item in the list is 5, not 6
# dice_num = randint(1, 6) #randint includes the last number, so it will never equal 6
# print(dice_imgs[dice_num]) #this will never print the last item in the list, so it will never print the last item in the list

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994: 
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# #the problem is that 1994 is not included in the if statement, so it will never print the statement 

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# #the error is that the input is a string, so it can't be compared to an integer. Also, the print statement is not indented, so it will never print. Also, the print statement is not formatted correctly, so it will not

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# #the problem is that the word_per_page variable is being compared to a string, so it will never equal

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
# #the problem is that the b_list.append is not indented, so it will only append the last item in the