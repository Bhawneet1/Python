"""
 1. mutable- key donot change value can change
 2. duplicates - keys can't be duplicate but values can be
 3. order - insertion order is followed according to key not index just key
 4. heterogeneous - fully heterogeneous
"""

d={}
print(type(d)) # <class 'dict'>

# key-value pair
d={1:"hello"}

d = {10:100 , 20:200 , 30:300 , 40:400}
# keys as index values

print(d[10]) #100

# change value at key = 10

d[10]=1000
print(d[10])

# to add the value in dictionary
d.update({50:500})
print(d)

d[60]=600 # python automatically add the value
print(d)

del d[60] # delete the key:value
print(d)

del d[50]

for i in d:
  print(i) # print keys here 10,20,30,40
  print(d[i]) # access values

# shallow copy and deep copy

# deep copy
a=[1,2,3,4]
b=a
b[0]=100
print(a) #[100, 2, 3, 4] if we change b a also changes same as pass by reference

# shallow copy
a=[1,2,3,4]
b=a.copy()
b[0]=100
print(a) #[1, 2, 3, 4] no change as shallow copy


# methods

# 1. clear
d.clear()
# 2. copy
d2 = d.copy()
print(d2)
# 3. get
d = {10:100 , 20:200 , 30:300 , 40:400}
print(d.get(20)) # same as d[20]
# 4. items
print(d.items()) # ([(10, 100), (20, 200), (30, 300), (40, 400)])

