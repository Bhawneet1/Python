# any name with extention is file

# file handling means "CRUD" operations in file

# open
p=open(r'Y:/python/main.py')
print(p.read())

r = open("superman.txt",'w') # write but by default 'r' read if not exists and open in read mode gives error therefore open in write mode

# w will overwrite if everytime you change the text

r.write("Hello I am Bhawneet and I am writing inside this file")

r.close() # open then also close



s = open("superman.txt",'a')

s.write("I am appending something in existing")

s.close()

# append use to add to existing text not overwrite

# 'x'  mode is used only to create a file

with open("superman.txt","r") as f:
  content = f.read()
  print(content)