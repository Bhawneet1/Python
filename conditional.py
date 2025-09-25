#only executes one code of block based on condition
# flow control

#any one excutes at a time
#precedance if > elif >else
money = int(input("please give me the money :- "))

if money == 10:
  print("I will have a choco bar")
elif money == 20:
  print("I will have a mango dolly")
else:
  print("I will have both")


#Q1 accept two numbers and print greatest between them
a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))

if a>b:
  print(f"{a} is greater than {b}")
elif b>a:
  print(f"{b} is greater than {a}")
else:
  print("Both the numbers are same")


#Q2 take gender as input and print greeting based on it "Good moring sir"

gender = str(input("Enter the gender(M/F):"))

if gender=="M" or gender == 'm':
  print("Good morning sir")
elif gender == 'F' or gender == 'f':
  print("Good Morning maam")
else:
  print("Unidentified gender")  


#Q3 accept integer and classify as odd or even

num = int(input("Give a number input:"))

if num%2==0:
  print(f"{num} is an even number")
elif num%2!=0:
  print(f"{num} is odd number")


#Q4 name and age as input and check valid voter or not

name = str(input("Please tell your name:")) #str by default

age = int(input("Now tell your age:"))

if age>=18:
  print(f"{name} is a valid voter")
else:
  print(f"{name} is not a valid voter")


#Q5 leap year or not

 #century divisible by 400
 #else divisible by 4

year = int(input(f"Tell your year :- "))

if year%100 ==0  and year%400 ==0: #century year
  print(f"{year} is a leap year")
elif year%100 !=0 and year%4==0:
  print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")

#Q6 temperature

temp = int(input("Enter the temperature: "))

if temp<0:
  print("Freesing cold")
elif temp>=0 and temp <10:
  print("Very cold")
elif temp>=10 and temp<20:
  print("cold")
elif temp>=20 and temp<30:
  print("plesant")
elif temp>=30 and temp<40:
  print("hot")
else:
  print("Very hot")