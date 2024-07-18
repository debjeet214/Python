import pandas
import math

# we can import by changing the name
import math as M

# we can import all functions of the module
from math import *

# we can import a specific functions of the module
from math import sqrt, pi

result = sqrt(9)
print(result)

#Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module.

print(dir(math))
print(dir(pandas))
