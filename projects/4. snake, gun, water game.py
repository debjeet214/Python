#     S W G
#     0 1 2
# S 0 D W L
# W 1 L D W
# G 2 W L D

import random

def check_win(user, comp):
  if comp == user:
    return 0
  elif comp == 1 and user == 2:
    return -1
  elif comp == 2 and user == 0:
    return -1
  elif comp == 0 and user == 1:
    return -1
  else:
    return 1

comp = random.randint(0, 2)
user = int(input("0 for 'snake' \n1 for 'water' \n2 for 'Gun' \nNow Enter your choice: "))

print("Computer: ", comp)
print("User: ", user)

score = check_win(user, comp)
if score == 0:
  print("It is a Draw")
elif score == 1:
  print("You Won")
else:
  print("You Lost")
