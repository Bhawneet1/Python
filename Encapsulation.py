# Access modifiers

# public
class Factory:
  a= "Pune"
  def show(self):
    print("Hello I am pune factory")

class Bhopal(Factory):
  def show2(self):
    print(super().a) # can access anywhere therefore not secure

obj = Bhopal()
obj.show2()


# protected
class Factory:
  _a= "Pune" # protected with _
  def _show(self): # protected with _
    print("Hello I am pune factory")

class Bhopal(Factory):
  def show2(self):
    print(super().a) # can access only in child class therefore not secure not really works in python just used as convention

# obj = Bhopal()
# obj.show2()


# private only inside class not outside
class Factory:
  __a= "Pune" # private with __
  def __show(self): # private with __
    print("Hello I am pune factory")

class Bhopal(Factory):
  def show2(self):
    pass
    # print(super().a) # can access only in child class therefore not secure not really works in python just used as convention

# obj = Bhopal()
# obj.show()
# 'super' object has no attribute 'a'
# can't access


# make a method to access the attribute outside class
class Factory:
  __a= "Pune" # private with __
  def show(self): # private with __
    print(Factory.__a)

obj = Factory()
obj.show()



class Demo:
  def __init__(self,name,age,salary):
    self.name=name
    self._age = age #protected
    self.__salary = salary # private
  
  def show(self):
    print("Inside class")
    print(f"name is {self.name}")
    print(f"age is {self._age}")
    print(f"salary is {self.__salary}")

obj = Demo("Bhawneet",21,500000)
obj.show()