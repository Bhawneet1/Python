a=5
b=20

#arithematic (Follow BODMAS)
print(a+b)
print(b-a)
print(a*b)
print(b/a)#float output
print(b//a)#int output
print(32/5)# 6.4
print(32//5)#6 truncate
print(5**2)# 5 power 2
print(32%5)#remainder here 2
print(12+4/2)

#assignment operators

a=23 #= is assignment

#compound assignment operators

a=20

a+=20
a+=40
a+=60
a/=2
a*=2
a**=1
a//=2
print(a)
#a=40 #re-assign


#comparison operators(Always true or false)
a=12
b=12

print(a==b)
print(a!=b)

a=12.1
b=12
print(a>b)
print(a<b)
print(23>=23)
print(45<=45)

#in strings comparison operators

print("A">"B") #compare the unicode values 65>66 False

print("ABC" > "ABD") #first compare first character then second and so on till same


#Logical operators

# comparison logical comparison

print((123 >=100)  and (34==34) and (45<90)) #both true therefore and operators returns true

print(12 != 12 or 23==45 or 67==56 or 10>5)
#any one true therefore true

print(not 12==12)