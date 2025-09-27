# polymorphism means many forms

class Animal:
  def show(self):
    print("hello I am Bhawneet ")

  # def show(self,name):# not function overloading in python therefore here also overridding (function with diff parameters is overloading)
    pass
class Human(Animal):
  def show(self):
    print("How are you ")
    # method overriding as the function in Human overrides the show() in Animal 

    # same name method then the child class method is executed

obj = Human()
obj.show()





# polymorphism - two types
# overidding
# duck typing

# duck typing
class Animal:
  def show(self):
    print("Hello jee")

class Human:
  def show(self):
    print("How are you")


obj1 = Animal()
obj1.show()

obj2 = Human()
obj2.show()

# obj1 and obj2 are two objects with diff classes , same function name diff functionality both functions print different