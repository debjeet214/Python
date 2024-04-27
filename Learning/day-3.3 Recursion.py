# recursion is basically calling the same function inside the function itself.

def fact(number):
  if number == 0 or number == 1:
    return 1
  else:
    return number *(fact(number-1))

fact(6)
