"""Some keywords
     1. Mutable - kisi bhi value ko change kar sakte hai creation ke baad
     2. Duplicates - allowed in list
     3. Ordered - maintains order
     4. Heterogeneous - multiple datatypes can hold in list"""


def hello():
  return "Hello how are you"
a= ["apple" , "banana" , "cherry"] #array like but heterogeneous

print(a[0]) # indexing

b = [12,13,14,15,16,34.5,True,hello()]
print(b[0:5]) #slicing
print(b[-1])#last index

l=[12,3,4,5,6]

l[0]=10

print(l)


# traverse over a list
# 1st way using index 
for i in range(len(b)):
  print(b[i])

# method 2
for i in b:
  print(i)

# print(dir(list))
# help(list)

#append(self, object, /) Append object to the end of the list.  

l = [1,2,3,4,5]
l.append(6) #at end
print(l)

l1 =  [1,3,4,5]
l1.insert(1,2) #index , value
print(l1)

l1.extend([20,25,30])# add multiple at end
print(l1)

l1.remove(2) # remove first occurance of 2
print(l1)

poped_el = l1.pop() # remove lat element and return it
print(l1)
print(poped_el)

index= l1.index(1)
print(index) #index of 1 is 0 but if element missing gives error

count = l1.count(20)
print(count)# count occurances of 20

l1.sort()
print(l1)
l1.reverse()
print(l1)
new_l1 = l1.copy()
print(new_l1)
l1.clear()
print(l1)#empty list


