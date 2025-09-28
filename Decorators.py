class Animal:
  @property
  def show(self):
    print("hello how are you")
    # decorator is used to inhance a function

obj = Animal()
obj.show # without the parenthesis we can call

def decorate(func): # pass function here hello as argument
  def wrapper(): 
    print("I will print myself before the function hello")
    func()
    print("I will print myself after the function hello")
  return wrapper


@decorate #custom decorator
def hello():
  print("hello I am Bhawneet Singh ")

hello()



def decorator(func):
  def wrapper(a,b): # we pass the parameter in the wrapper and function in decorator
    print("Before addition")
    func(a,b)
    print("After addition")
  return wrapper

@decorator
def addition(a,b):
  print(f"The addition is : {a+b}")


addition(10,20)





