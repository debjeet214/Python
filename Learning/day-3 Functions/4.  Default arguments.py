# We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.
 

# TYPE 1  (Here both default values are given to the argument so, even no value is taken, it will be executed with the default values)
def default_arg(x = 76, y=8):
  z = x*y
  return z# default arguments 
# 

default_arg()

# TYPE 2

def side(x = 24.56, y=20):
  z = x*y
  return z

default_arg(y = 10)   # but using like this will help to remove the order of argument.
# or default_arg(4) here 4 will be used as the value of the x now
