# on each member of a list , tuple

a= [1,2,3,4]

result = map(lambda x : x*2,a)

print(list(result))


b=[1,2,3,4]

result = map(lambda x : x**2 , b)

print(list(result))


# filter takes list , tuple

def even(a):
  if a%2==0:
    return True
  else:
    return False
  
a= [1,2,3,4,5,6,7,8,9]

result = filter(even,a) #function , list
print(list(result))


result = filter(lambda x : True if x%2==0 else False, a)

print(list(result))