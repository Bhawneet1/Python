# between classes
#inheritance allows a class to inherit properties and members from parent class

# reusability , structured  ,easy to maintain and extend

class Factory: #parent class / super class
  a= "I am a member inside Factory"

  def hello(self):
    print("hello I am a method inside Factory")

class Factorypune(Factory):#inheritance (child class / subclass)
  pass

obj = Factory()
print(obj.a)
obj.hello()

obj1 = Factorypune()
print(obj1.a) # works as inheritance is there and can access both a and hello()
obj1.hello()


## constructor of parent access by child as well

class Animal:
  def __init__(self,name):
    self.name = name
  
  def show(self):
    print(f"Hello your name is {self.name}")

class Human(Animal):
  pass


person1 = Human("Bhawneet")

person1.show()


def __init__(self,name):
    self.name = name
  
def show(self):
    print(f"Hello your name is {self.name}")

class Human(Animal):
  def __init__(self, name,age):
    super().__init__(name) # super() target animal class and get name from there
    self.age = age
  def show(self):
    print(f"you are human with {self.name} and  {self.age} ")
  
human1 = Human("Bhawneet" , 21)
human1.show()


## Types of inheritance

# single - one parent and one child
# Multiple - two parent one child
# Multi-level 



# Mutiple

class Animal: 
  name1 = "lion"

class Human:
  name2 = "Bhawneet"

class Robots(Animal , Human):
  name3 = "Charlie"

obj = Robots()
print(obj.name1)
print(obj.name2)
print(obj.name3)
class Animal: 
  def __init__(self,name):
    pass

class Human:
  def __init__(self,name,age):
    pass

class Robots(Animal , Human):
  name3 = "Charlie"

