# Way 2

def decorator_func(printing):    # this is the decorator function
  def inner():                   # inner (any name can be given) function that will be returned
    print("Before")          # adding extra functionality
    printing()               # existing function called
    # more functionality added
    print("Bye for now!!")
  return inner     # this will be returned 


def printing():      # actual exisitng function
  print("Hello")
  print("How are you?")

greet = decorator_func(printing)    # To store the new value into an different function
greet()                             # finally calling it
