import os
import string
import random

xstr = input("Enter the line of string you want to take input: ")
Act_Word = xstr.split(" ")
print(Act_Word)

Hardness = int(input("Enter the hardness level from 1 to 8: "))
coding_type = input("Enter what you want, enter 1 for encoding & 0 for decoding: ")
coding_type = True if (coding_type == '1') else False
print(coding_type)

if(coding_type):
  Nw = []
  for word in Act_Word:
    if (len(word)>=3):
      r1 = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=Hardness))
      r2 = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=Hardness))
      stnew = r1 + word[1:] + word[0] + r2
      Nw.append(stnew)
    else:
      Nw.append(word[::-1])
  print(" ".join(Nw))

else:
  Nw = []
  for word in Act_Word:
    if (len(word)>=3):  
      stnew = word[3:-3]
      stnew = word[-1] + word[:-1]
      Nw.append(stnew)
    else:
      Nw.append(word[::-1])
  print(" ".join(Nw))
