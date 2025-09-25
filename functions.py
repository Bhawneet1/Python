# block of code whenever we call
def hello():
  print("Hello 👋 ")

hello() #if no call therefore not run
hello()

# parameters and arguments

# parameters inside definition(things you pass)
# arguments passed as input when called (thing you provide while call)


def sum(a,b):
  print(f"sum of {a} and {b} is {a+b}")

sum(12,13) # these are positional arguments
sum(12,45)

def greet(name ,age):
  print(f"Hello {name} 👋 , your age is {age}")

greet(age=21 , name="Bhawneet")
#not positional as the position changed they are called keyword argument as passed along with keywords


def sum2(a,b=45):
  print(a+b)

sum2(20)
#default argument if not passed taken as default
sum2(20,56) #replace default

def pallindrome(st):
  rev = ""
  for i in range(len(st)-1,-1,-1):
    rev+=st[i]
  if rev == st:
    print("It is pallindrome ")
  else:
    print("Not a pallindrome ")


pallindrome("NAMAN")
pallindrome("CURSOR")


def hello():
  return "Hello how are you"

ans =hello()# return value over here
print(ans)