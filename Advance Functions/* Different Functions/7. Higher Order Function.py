# higher order function:: those that take other functions as their parameters or those functions that return other functions are called higher-order function

def add(n1, n2):
  return n1+n2

def display(func):
  print(func(10, 20))

display(add)
