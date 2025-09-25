# print hello world n times

n = int(input("Enter number: "))

for i in range(n): #0 to n-1
  print("Hello World! ")


# print natural numbers upto n

for i in range(1,n+1):
  print(i)


# reverse loop n to 1
for i in range(n,0,-1):
  print(i)

# print table

for i in range(n,n*10+1,n):
  print(i)

for i in range(1,11):
  print(n*i)


# sum of n terms

sum=0

for i in range(1,n+1):
  sum+=i
print(sum)


# factorial

prod = 1

for i in range(1,n+1):
  prod*=i

print(prod)


# even and odd numbers sum

even_s = 0
odd_s=0

for i in range(1,n+1):
  if i%2==0:
    even_s+=i
  else:
    odd_s+=i

print(even_s , odd_s)


# print all factors of n

for i in range(1,n+1):
  if n%i==0:
    print(i)


# check if perfect number or not
# perfect number whose sum of factors equal to number
# not consider number itself as factor

sum=0
for i in range(1,n):
  if n%i==0:
    sum+=i

if sum==n:
  print("Yes it is perfect ")


# check prime or not

count= 0 

for i in range(1,n+1):
  if n%i == 0:
    count+=1

if count == 2: #exactly 2 factors 1 and number itself
  print("It is a prime number")

else: 
  print("Not prime ")



# reverse a string

name = str(input("Enter a word to check pallindrome: "))

for i in range(len(name)-1,-1,-1):# from len-1 index to 0 step -1
  print(name[i])

#check pallindrome

b=""
for i in range(len(name)-1,-1,-1):
  b+=name[i]

if name == b:
  print("Yes it is pallindrome")
else:
  print("it is not pallindrome")


# count digits , chars , specialchars in a string

a="abcdefg12345678hij&^%&*()"

char = 0
dig = 0
spec = 0
for i in a:
  if i.isdigit():
    dig+=1
  elif i.isalpha():
    char+=1
  else:
    spec+=1

print(char , dig, spec)

# directory of strings to get methods of strings
print(dir(str))