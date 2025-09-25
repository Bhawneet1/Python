import random

num = random.randint(1,10)



turns = 0
while True:
  guess = int(input("Please guess a number between 1 to 10 "))
  if num == guess:
    print("Yeh you won 🥳🥳")
    turns+=1
    break
  elif num < guess:
    turns+=1
    print("go a little lower")
    
  elif num>guess:
    print("go a bit higher ")
    turns+=1
  else:
    print("Sorry you are wrong😔😔")
    turns+=1

print(f"You took {turns} turns to win ")