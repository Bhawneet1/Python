
#seperate digits in a number

# eg number = 256 seperate 2 5 6 

a=int(input("Give me a multiple digit number: "))

while a>0:
  digit = a%10
  print(digit)
  a=a//10 # floor division 


# reverse a number
a=int(input("Give me a multiple digit number: "))
rev=0

while a>0:
  rev = rev*10 + a%10
  a=a//10
  

print(rev)

# check pallindrome number 

#since our a is now 0 we need to make copy first

a=int(input("Give me a multiple digit number: "))

copy = a
rev=0

while a>0:
  rev = rev*10 + a%10
  a=a//10

if rev == copy:
  print("Pallindome hai ")
else:
  print("Nahi hai ")