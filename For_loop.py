# for loop and while loop

# for loop when you know number 
# while works on condition

# range three things 
# range(start , stop ,step)

a= range(1,21,1) #stop must be one more than required

# in range first and last value is default 0 
for i in a:
  print(i)


for i in range(21):
  print(i)

# from 16 to 1

for i in range(16,0,-1): #neg steps therefore one less than required
  print(i)


n = int(input("Enter a number for which you need table: "))

for i in range(n,n*10+1,n):
  print(i)


a="Bhawneet"
n=len(a)
for i in range(n):
  print(a[i])


for i in range(1,21):
  if i==15:
    break
  else:
    print(i)
# will print till 14 then break
# break requires else if break works else not work 

for i in range(1,21):
  if i==15:
    continue
  else:
    print(i)
# will print till 14 then skip 15 then from 16 print