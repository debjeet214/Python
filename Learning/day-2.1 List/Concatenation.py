# concatination of list:

# way 1

list1 =[21, 44, 39, 76, 98, 56, 37]
list2 = [1, 30, 9, 7]

list3 = list1 + list2
print(list3)

# way 2

list1.extend(list2)   # this will extend the list2 inside list1 making it lenghtly
print(list1)
