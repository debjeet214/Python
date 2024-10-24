# The search() function searches the string for a match, and returns a Match object if there is a match.

import re
txt = "The rain in Spain"
x = re.search("\s", txt)  # this means it will search for the first white-space in the string 
print("The first white-space character is located in position:", x.start()) # This will return the starting index value of the string

# example 2

import re
txt = "The rain in Spain"
x = re.search("Spain", txt)
print(x)                     # this will return the actual match object and description 
print(x.start())             # this will return the starting index of the search thing.

# o/p
# <re.Match object; span=(12, 17), match='Spain'>
# 12
