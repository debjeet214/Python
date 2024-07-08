# docstring has to be decleared below the fucntion declaration and it can be accessed by .__doc__ keyword.

# Python Comments ::  Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.

# Python docstrings ::  As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code.
# We can access these docstrings using the doc attribute.

def square(n):
  '''Takes in a number n, returns the square of n'''   # this is a doc string which is not similar to comments.
  print(n**2)
square(5)
print(square.__doc__)
