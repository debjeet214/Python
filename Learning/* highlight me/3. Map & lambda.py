# map: The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax: map(function, iterable)

# way 1 using the function & loop to create a new list from an another list element's cube
def cube(x):
  return x * x * x

num = [ 3, 6, 9, 00, 1, 21, 3, 5, 8, 14, 27]
newlist = []
for i in num:
  newlist.append(cube(i))
print(newlist)

# way 2 using map
newlist = list(map(cube, num)) # map simply take the old list and perform a function on each element & create a new element.
print(newlist)

# way 3 using lambda function without function definition
newlist = list(map(lambda x: x * x * x, num))
print(newlist)
