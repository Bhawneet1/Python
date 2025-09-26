from pathlib import Path
import os

def readFileAndFolder():
  path = Path('')
  items = list(path.rglob('*'))
  # recusrive glob will give all files in directory
  for i,items in enumerate(items):
    #index i and values items
    print(f"{i+1} : {items}")


def createFile():
  try:
    readFileAndFolder()
    name = input("please tell your file name :- ")
    p = Path(name)
    if not p.exists():
      with open(p,"w") as fs:
        data = input("What you want to write in this file: ")
        fs.write(data)
      print(f"FILE CREATED SUCCESSFULLY")  
    else:
      print(f"This file already exists")
  except Exception as err:
    print(f"An error occured as {err} ")



def readFile():
  try: 
    readFileAndFolder()
    name = input("Enter the file you want to read:- ")
    p= Path(name)

    if p.exists() and p.is_file:
      with open(p,"r") as fs:
        data = fs.read()
        print(data)
      print("Readed successfully")
    else:
      print("The file does not exists")

  except Exception as err:
    print("Some error occured as {err} ")



def updateFile():
  try:
    readFileAndFolder()
    name = input("Enter the file you want to update:- ")
    p = Path(name)

    if p.exists() and p.is_file():
      print("press 1 for changing the name of your file :- ")
      print("press 2 for overwritting the data of your file :- ")
      print("press 3 for appending some content in your file :- ")

      res = int(input("please tell your response :- "))

      if res == 1:
        name = input("Enter your new file name :- ")
        p2 = Path(name)
        p.rename(p2)
      if res == 2:
        with open(p , 'w') as fs:
          data = input("Tell what you want to write this will overwrite the data ")
          fs.write(data)
          print("Successfully overwritten ")
      if res == 3:
        with open(p ,"a") as fs:
          data = input("Enter data you want to append ")
          fs.write(" "+data)
          print("Successfully appended ")
  except Exception as err:
    print(f"An error occured as {err}")



def deleteFile():
  try:
    readFileAndFolder()
    name = input("Which file you want to delete :- ")
    p = Path(name)

    if p.exists() and p.is_file():
      os.remove(name)
      print("File removed successfully")
    else:
      print("No such file exists")
  except Exception as err:
    print(f"An error occured as {err}")





print("press 1 for creating a file ")
print("press 2 for reading a file ")
print("press 3 for updating a file ")
print("press 4 for deleting a file ")

check = int(input("Please tell your response:- "))

if check == 1:
  createFile()

if check == 2:
  readFile()

if check == 3:
  updateFile()

if check == 4:
  deleteFile()
