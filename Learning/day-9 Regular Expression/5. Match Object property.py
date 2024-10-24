# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

# SPAN
# Prints the index fo the first occurace of the matching string.
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# GROUP
# Prints the word that matches with the matching condition string.
txt = "The rain in Spain"
x = re.search(r"\bi\w+", txt)
print(x.group())

# STRING
# prints the whole string that is passed into the function
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
