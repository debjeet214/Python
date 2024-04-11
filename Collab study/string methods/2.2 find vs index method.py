txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

y = txt.index('hi')
z = txt.find('hi')   # this will not return any error


# The index() method finds the first occurrence of the specified value. The index() method raises an exception if the value is not found means error.
# The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found whereas index method shows error if the value is not there.
