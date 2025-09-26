# print positive and negetive elements of list

l = [-1,-2,-3,4 ,5 ,6 ,7 ,-9,-10 ,0 ]

for i in range(len(l)):
  if l[i]<0:
    print(f"{l[i]} is negetive ")
  elif l[i]>0:
    print(f"{l[i]} is positive ")
  else:
    print(f"{l[i]} is zero")



# Mean of list element

l = [1,2,3,4,5,6,7,8]

sum=0
for i in range(len(l)):
  sum += l[i]
print(sum / len(l))


# find greatest element and print it's index too

l = [12,16,13,19,17]

maxi = l[0]

# for i in range(len(l)):
#   maxi = max(maxi , l[i])

# print(f"Max element is {maxi} at index {l.index(maxi)}")

index = 0
for i in range(1,len(l)):
  if maxi < l[i]:
    maxi = l[i]
    index = i
    

print(f"Max element is {maxi} at index {index}")


# find second largest 

second = l[0]
maxi = l[0]
index = 0
index_2=0

for i in range(len(l)):
  if maxi<l[i]:
    second = maxi
    index_2 = index
    maxi = l[i]
    index = i
  elif l[i]>second:
    second = l[i]
print(f"Second largest element is {second} at index {index_2}")


# check if list is sorted or not
a = [12,15,14,15,16,17]

for i in range(len(a)-1):# if here len(a) therefore out of bound i+1
  if a[i] < a[i+1] :
    continue
  else:
    print("Your list is not sorted")
    break
  
else:
  print("Your list is sorted")