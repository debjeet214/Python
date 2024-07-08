# filter = The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. Means, if we apply a specific filter on a list elements then, it will filter out them by returning true or false for each elements. and only return the true elements in the result.

def filter_function(a):
  if a >10:
    return a
  else:
    return 0
  
num = [ 3, 6, 9, 10, 13, 21, 3, 51, 8, 14, 27]
newlist = list(filter(filter_function, num))   # applying the function on each elements to filter
print(newlist)

# reduce = this helps to reduce the list element one by one and makes it easy.

from functools import reduce
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)
# Print the sum
print(sum)
