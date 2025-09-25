# Hello I am Bhawneet how are you
"""THIS IS A MULTILINE COMMENT"""
print("Hello World")


SheriyansSchool = "students" #Pascal Scale
sheryansSchool = "students" #camel case
sheryans_school = "students" #snake case

a=5
print(type(a))

b=5.5
print(type(b))

c=12/3 #p/q always is float
print(type(c))

v=34j #complex
print(type(v))

st = "abdkbkvb 85285825 %&%&@($)"
print(type(st))

p=True
print(type(p))

a= 'A'
print(ord(a)) #the hex vlaue of A is 65 or unicode

b = 65
print(chr(b))#unicode to char

a="SHER"
print(a[1]) #indexing

print(a[3],a[-1]) #-1 means last

#string slicing
b= "SHER CODER"
print(b[0:4:1])# start : stop(workers till mentioned-1 index) : step

print(b[5::1]) #default end till last index


a=12
print(type(a))

a=str(a)# type explicit conversions 
print(type(a))

c=10
print(bool(c)) #always true if any number or string then true 


"""
falsy values
False
0
0.0
""
[]
()
{}
"""
#truthy values other then falsy

print(12/3) #implicit type conversion to float

name = "Bhawneet"

age = 21

print(f"My name is {name} and my age is {age}") #formated string

#input 
age =int(input("Hello what is you age?")) #converted to int
#default data type is string
print(type(age),age)