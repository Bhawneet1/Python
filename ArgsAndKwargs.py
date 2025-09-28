def addition(a,b):
  print(a+b)

addition(10,20)

# if I need to increase the arguments but not in function just in input

# therefore args

def addition(*args):
  # we get tuple as args here
  sum=0
  for i in args:
    sum+=i
  print(sum)

addition(1,2,3,4,5,6)



# keyword arguments

def addition(**kwargs):
  #here we get dictionary as it is key value pair
  for i in kwargs:
    print(f" {i} : {kwargs[i]}")

addition(a=12,b=30,c=30)



def decorator(func):
  def wrapper(*args,**kwargs): # we pass the parameter in the wrapper and function in decorator
    print("Before addition")
    func(*args,**kwargs)
    print("After addition")
  return wrapper

@decorator
def addition(a,b):
  print(f"The addition is : {a+b}")


addition(10,20)
