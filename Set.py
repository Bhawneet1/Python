"""
 1. mutable
 2. no duplicates
 3. unordered - no index value
 4. heterogeneous - semi-hetrogeneous
"""

"""
each value is hashed using hash() function
"""

s={} # dictionary

s={1,2,3,4} #set if we fill it

c= hash((1,2,344))
print(c)

# can't traverse using loops as no order
# as hash value change everytime

a={1,8,9,2,3,4,5,6,7}

for i in a:
  print(i) # all depend on hash value


# methods
s={1,2,3}

s.add(4) # add at end
print(s)

s.remove(2) # search hash value of 2 and remove
print(s)

s.pop() # as hash is random therefore random remove min hash value

print(s)

s.clear()
print(s)

# operations on set

# 1. Union
a={1,2,3,4,5}
b={4,5,6,7,8}

print(a.union(b)) #{1, 2, 3, 4, 5, 6, 7, 8} intersection just once
print(a|b) #union

# 2. intersection

print(a.intersection(b)) #{4,5}

print(a&b) #same as intersection

# 3. difference
print(a.difference(b)) #{1, 2, 3} a-a intersection b
print(b.difference(a)) #{8, 6, 7}

print(a-b)
print(b-a)

# 4.symmertric difference 

print(b^a) #union - intersection
print(b.symmetric_difference(a))
