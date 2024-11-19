# map function
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

nums = [5, 3, 11, 21, 4, 6]
def square(num):
  return num*num
mapped_obj = map(square, nums)
print(list(mapped_obj))


# use lambda for this 
nums = [5, 3, 11, 21, 4, 6]
mapped_obj = map(lambda num:num**2, nums)
print(list(mapped_obj))

# find the square of only the even nums 
nums = [5, 3, 11, 21, 4, 6]
result = map(lambda num: num**2, filter(lambda num: num % 2 == 0, nums))
print(list(result))
