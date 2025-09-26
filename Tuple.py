"""
 1. Immutable- can't reassign
 2. Duplicates - allowed
 3. Ordered - matters
 4. Heterogenous - multiple datatypes
"""


a=(1,2,3,4,5,2,5,5,5,5)
#'tuple' object does not support item assignment
# a[0]=10

print(a)

for i in range(len(a)):
  print(a[i])

index = a.index(5)
print(index) #index of 5 is 4

count = a.count(5)
print(count) # here 5 is repeated 5 times


# tuple unpacking
a,b,c,d = (1,2,3,4)

# a=1 b=2 c=3 d=4
print(a)

a=(1)
print(type(a)) # <class 'int'>

a=(1,)
print(type(a)) # <class 'tuple'>