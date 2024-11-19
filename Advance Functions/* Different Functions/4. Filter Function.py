# filter function  
# it takes a function and iterables to exacute the function on the iterable values

data = [12, 45, 67, 32, 100, 53, 7, 4]
def even(num):
  if num%2==0:
    return True
  else:
    return False

print(list(filter(even, data)))

# making it inline function
print(list(filter(lambda num:num%2!=0, [12, 41, 67, 40, 100, 53, 7, 4])))
