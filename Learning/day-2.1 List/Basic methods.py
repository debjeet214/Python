list_val = [1, 65, -3, 0, 76, 21, 8, 1]

list_val.append(7)   # this method add a value at the end
list_val.insert(0, 87)  # to add a value at any index position of the list
list_val.remove(7)   # to remove a value from the list, if there are two same values it will then remove the first one.

print(list_val.index(0))    # this is used to retun the index no. of the given value
print(list_val.count(1))    # this will return the no. of times a given value repeats in the list

print(22 in list_val)  # to find a item in the list which will return true or false

print(len(list_val))  # check how many elements are in the list.

list_val.sort()   # sort the array in ascending order
print(list_val)

list_val.sort(reverse = True)   # sort the array in descending order by reversing it
print(list_val)

list_val.reverse()   # reverse the order of the list elements
print(list_val)

list_val.clear()      # this will clear all the elements in the list
print(li)
