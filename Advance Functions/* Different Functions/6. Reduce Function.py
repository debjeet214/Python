# reduce function : reduce the values in the list one by one
import functools
nums = [1, 45, 32, 9, 21, 40, 90]
result = functools.reduce(lambda num1, num2: num1+num2, nums)
print(result) # addition value

# ex2 :: return the max value
def max(num1, num2):
  if num1 > num2:
    return num1
  else:
    return num2
result = functools.reduce(max, nums)
print(result)
