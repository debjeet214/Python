# to update a tuple we first change the tuple into list and then made changes and finally we are converting the list into tuple again making it updatable

tuples = (1, 23, 54, 9, 71, 22, 6)
temp = list(tuples)
temp.append(333)
print(temp)
temp.pop(-1)
temp.insert(-1, 21)
tuples = tuple(temp)
print(tuples)
