# The findall() function returns a list containing all matches.

import re

txt = "The rain in Spain"
x = re.findall("in", txt)
print(x)
# This will return all the matching  -> ['in', 'in', 'in']

# attempt 2
txt = "The rain in Spain"
x = re.findall("int", txt)
print(x)

# if there is no matrhing then it will return a empty set. -> []
