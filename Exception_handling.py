# error that occurs due to some error in code

# Types

# 1. syntax error
#print("Hello" # no bracket therefore error

# 2. indentation error
# a=12
# if a==12:
# print("Hello") #no space therefore error

# 3. tab error

# except these three are exception and that we can handle

a= int(input("Tell your number :- "))

print(10/a) #  division by zero as we give 0 in a therefore we need to handle this exception

print("No exception I am here")
# if exception then we can't proceed further(can't come here if 0 is input) therefore handle the exception here


# handling try except 

b =  int(input("Tell your number :- "))

try:
  print(10/b)
except ZeroDivisionError:
  print("Sorry you can't divide by 0 ⚠️")


print("I will come here always as try except in code")


# there are many errors therefore we write except as

c= (input("Enter a number: "))
try:
  print(10/c)
except Exception as err:
  print(f"Sorry there is an error as {err}")

print("I will come here always as try except in code")

# add else also

d= int(input("Enter a number: "))
try:
  print(10/d)
except Exception as err:
  print(f"Sorry there is an error as {err}")

else:
  print("There is no exception") # if try works and except donot work then else work 

# finally always run
e= int(input("Enter a number: "))
try:
  print(10/e)
except Exception as err:
  print(f"Sorry there is an error as {err}")

else:
  print("There is no exception")

finally:
  print("I will always run")




# raise throw error manually

age = int(input("Tell your age "))

try:
  if age<10 or age>18:
    raise ValueError("Your age must be between 10 and 18")
  else:
    print("Welcome to the club")
except Exception as err:
  print(f"An error occured as {err}")

print("The club will start soon")