# Sets are unordered collection of data items. They store multiple items in a single variable. 
# Set items are separated by commas and enclosed within curly brackets {}. 
# Sets are unchangeable, meaning you cannot change items of the set once created. 
# Sets do not contain duplicate items & don't maintain the order of input values.

set1 = {"hi", 10, 4, 'D', 65.098, 21, "Mitali", 21}
print(set1)

set2 = {21, 32, 73, 9, 21, 76.08, 88, 9, 73}
for i in set2:
  print(i)   # only print the uniqu values in unordered condition.

print(len(set2)) # This will return 6 cause, it won't count the duplicate values here.

set_initialize = {}
print(type(set_initialize))    # this will be a dictionary as both have same syntax 

# To get a empty Set we have to mention it like this
set_n = set()
print(type(set_n)) # now it will return clss set.
