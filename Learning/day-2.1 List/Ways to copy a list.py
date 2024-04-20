list_val = [1, 65, -3, 0, 76, 21, 8, 1]
print(list_val)

# ways to copy the list to another list
new_list = list_val
new_list[0] = 999
print(new_list)
print(list_val)  # here the actual list also changed here as no copy  is made by it happens by referrence

# second way to do copy
list_val2 = [1, 6, -3, 0, 76, 21, 8, 1]
new_list2 = list_val2.copy()
new_list2[0] = 888
print(new_list2)
print(list_val2)   # Here it is not chnaging the actual values of the actual list but it just change the copy of the actual one
