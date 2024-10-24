# The split() function returns a list where the string has been split at each match:

import re

txt = "The rain in Spain"
x = re.split("\si", txt)  # this means return the string by splitting if there is a 'i' right after a white-space.
print(x)

# o/p -> ['The rain', 'n Spain']
# herev in the string there is only one i right after a white-space of a string which is 'in', so splitted from there.

# ex -2
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1) # this split the sentencxe when there is a white space, but putting 1 will only split the string from first white-space only
print(x)  #  -> ['The rain', 'n Spain']

#example 3
import re

txt = "The rain in Spain"
x = re.split("jj", txt) 
print(x)

# if there is no matching for splitting, then it will return the whole string once. -> ['The rain in Spain']
