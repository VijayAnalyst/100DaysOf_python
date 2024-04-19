#class a blueprint for a cars

#class User:
#  pass

#user_1 = User()
#user_1.id = "001"
#user_1.username = "angela"

#print(user_1.username)

#user_2 = User()
#user_2.id = "002"
#user_2.username = "jack"

#calss Car:
#  def __init__(self):
#    initialize attributes to the object

#class User:
#  def __init__(self):
#    print("new user being created...")

#user_1 = User() #o/p: new user being created...
#user_1.id = "001"
#user_1.username = "angela"
#print(user_1.username) #o/p: angela
#user_2 = User() #o/p: new user being created...
#here we are creating a new user everytime we create a new object

#Attribute
#class car: #created a car class
#  def __init__(self, seats): #created a method 
#    self.seats = seats #created a attribute
# construtor is combination of init and class. Methods and attributes 
 # def enter_race_mode(self): #created a method
 #   self.seats = 2
    

#my_car = Car(5) #created a object
#print(my_car.seats) #o/p: 5
#my_car.enter_race_mode()

class User: #creat a class called user
  #PascalCase : It means that the first letter of each word is capitalized
  #camelCase : It means that the first letter of each word is not capitalized
  #snake_case : It means that each word is separated by an underscore character
  def __init__(self, user_id, username): #init method is a special method that is called when we create an object from a class 
    #self is a blank object that was created before we called the init method
    #construtor function : a function that is called when we instantiate an object from a class
    self.id = user_id #attribute, here we are assigning a value to the attribute
    self.username = username 
    self.followers = 0
    self.following = 0

  def follow(self, user): #calling a method
    user.followers += 1
    self.following += 1

user_1 = User("001", "angela")
user_2 = User("002", "jack")
print(user_1.username)#o/p: angela
print(user_1.id) #o/p: 001
user_1.follow(user_2)
print(user_1.followers) #o/p: 0
print(user_1.following) #o/p: 1
print(user_2.followers) #o/p: 1
print(user_2.following) #o/p: 0

def funcation(): #declaring a function
  pass #do nothing, Here pass means do nothing it will be used when we are not sure what to do with the function it is just a placeholder

print("hello")

class Car:
  def __init__(self, make, model, year, color):
    self.make = make
    self.model = model
    self.year = year
    self.color = color

  def drive(self):
    print("This " + self.model + " is driving")

  def stop(self):
    print("This " + self.model + " is stopped")