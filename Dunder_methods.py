# starts and ends with __ is dunder

class Animal:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def __str__(self):
    return "Hello how are you"
  
  # def __add__(self,other):# self one object other another object
  #   return f"sum of ages is {self.age + other.age}"
  
  def __add__(self,other):
    # pass other as tuple
    # if multiple animals > 2
    sum = 0
    for i in other:
      sum+=i.age
    return f"sum of ages is {self.age+sum}"

obj = Animal("Lion",12)
print(obj) # we can only print object this way

obj2 = Animal("Dolphin" , 14)
# print(obj + obj2 )

obj3 = Animal("Tiger",15)
print(obj + (obj2,obj3))