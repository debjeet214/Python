marks = [32, "Mitali", True, 69, "Debjeet loves ", 21, 78]

print(marks)
print(type(marks))
print(marks[4])
print(marks[1])
print(marks[0])

# negative indexing ( all the below lines will give same output but using different logics )
print(marks[-4])
print(marks[len(marks)-4])
print(marks[6-4])
print(marks[2])

# finding a value from the list
if 69 in marks:
  print("yes it is here")
else:
  print("there is no 69")

print(22 in list_val) # same thing of finding a vlaue in the list but it will return true or false

# printing values of list in agap sequence

num = [ 3, 76, 98, 00, 1, 21, 34, 65, 89, 47, 73]

print(num)
print(num[:]) # it will print all the values in the list

print(num[1:8])  # this will print all the values ranging from index 1 to 7
print(num[1:8:2])  #this will print 1 to 7 indexed values with 2 gapping
