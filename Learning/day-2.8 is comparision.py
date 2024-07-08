# In Python, is and == are both comparison operators that can be used to check if two values are equal. However, there are some important differences between the two that you should be aware of.

#The is operator compares the identity of two objects, while the == operator compares the values of the objects. This means that is will only return True if the objects being compared are the exact same object in memory, while == will return True if the objects have the same value.

# for tuple, integer same values it will show true cause they are mutable. 
a = 3
b = 3

print(a is b) # exact location of object in memory
print(a is 3) # exact location of object in memory
print(a == b) # compare only value
print("\n")

# but in case of list or any other type of things it will return false while comparing.
a = [3, 5, 12]
b = [3, 5, 12]

print(a is b) # exact location of object in memory
print(a == b) # compare only value
