# normal for looping

name = " debosmita"
for characters in name:
  print(characters)
  

# for loop to print the elements and the characters of each elements

marks_list = ["debjeet", "Mitali", "Ankita", "Sourago", "Ditipriya"]
for names in marks_list:
  print("\n")
  if(names == "Mitali"):
    print(names, "You are my love babe.")
  for i in names:
    print(i)
    
# this , end = "" will print all the elements of a single iteration in a same line not in a different row.
# range in the for loop

for i in range(10):   # this will print from 0 to 9 total 10 times
  print(i, end = ' ')
print("\n")

for j in range(5, 10):      # this will print from the given range here from 5 to 10-1
  print(j, end = ' ')
print("\n")

for k in range(3, 12, 2):     
  print(k, end = ' ')
