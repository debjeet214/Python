Enumerate is a built-in function in python that allows you to keep track of the number of iterations (loops) in a loop. This enumerate object contains a count (from the start, which always defaults to 0) and a value obtained from iterating over the iterable object.

marks = [12, 56, 32, 98, 12,  45, 1, 4]

# this require a index variable to count
index = 0
for mark in marks:
  print(mark, index)
  if(index == 3):
    print("Harry, awesome!")
  index +=1

# emurate just count it by itself
for index, mark in enumerate(marks, start=1):
  print(mark, index)
  if(index == 3):
    print("Harry, awesome!")
