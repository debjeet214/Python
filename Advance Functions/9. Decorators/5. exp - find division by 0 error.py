def decor(func):
  def inner(*args):
    for num in args[1:]:
      if num == 0:
        return "Can not divide by 0"
      return func(*args)
  return inner

@decor
def division(a,b):
  return a/b
@decor
def div2(a, b, c):
  return a/b/c     # first a will be divided by b, then the result will be divided by c

print(division(10,2))
print(division(0,50))
print(division(10,0))
print(div2(10,2,3))
print(div2(10,0,3))
print(div2(10,0,0))
print(div2(0,5,3))

''' output 
5.0
0.0
Can not divide by 0
1.6666666666666667
Can not divide by 0
Can not divide by 0
0.0
'''
