
# imperative approach

print(10+20)

a=20
b=30
print(a+b)

# functional approach

def addition(a,b):
  print(a+b)

addition(10,20)

# object oriented programming
# based on concept of objects
# code reusable
# security
# management system


## classes is a blueprint 
#  attributes and members
class Factory:
  a=12 # attribute (local scope inside class)
  def hello(self): # method
    print("How are you")
    #self capture the object like this in cpp
  
  print("Hello how are you I am getting intialized")

print(Factory().a)
Factory().hello()

## object is an instance of class

obj = Factory()

print(obj.a)
obj.hello()


## constructor
# accept parameters from constructors
# runs automatically when called class and target object location

class Factory:
  def __init__(self,material , zips ,pockets ):
    self.material = material
    self.zips = zips
    self.pockets = pockets
    # constructor
  
  def show(self):
    print(f"your object details are {self.material} , {self.zips} , {self.pockets}")

reebok =Factory("leather" , 3,2)

# in self we provide location in RAM eg 100
# 100.material = "leather"
# 100.zips = 3
# 100.pockets = 2

print(reebok.pockets)
print(reebok.show())


class Animal:
  name = "lion" # data member
  def __init__(self,age):# constructor
    self.age =age #instance attribute
  
  def show(self): # accepting self therefore instance method
    print(f"How are you your age is {self.age} ")

  @classmethod #decorator to define class methods

  def hello(cls):# target class location
    print("How are you brother")

  @staticmethod # regular function placed in class

  def static():
    print("Hello from static")
    

obj = Animal(12) 

obj.show()
obj.hello()
obj.static()
