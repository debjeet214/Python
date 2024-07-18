# converting the 2 num addition to 3 num addition

def decorator(func):
  def inner():
    result = func()
    num3 = float(input("Enter third number: "))
    result = result + num3
    return result
  return inner         # without changing the addition() function, we change the functionality

def addition():        # function to add 2 values
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  return num1 + num2

sum = decorator(addition)
print(sum())


# we can shorthand the ending like this
```
@decorator
def addition():        # function to add 2 values
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  return num1 + num2

addition()
```
