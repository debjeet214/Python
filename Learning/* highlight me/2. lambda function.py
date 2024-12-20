#In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:
# syntax => lambda arguments: expression
# lamda is just the simple and short form of the normal defined functions but it is expressed in one line without defining them. here, only the argument and expressions ahs to be send.

# Example 1:
double = lambda x: x * 2
print(double(5))

# Example 2: area of circle = A = π r²

x = int(input("Enter the radius of the circle: "))
cirlce_area = lambda x, y = 3.14:x*x*y
print(type(cirlce_area))
print(cirlce_area(x))

# example 3
avg = lambda x, y, z: (x + y + z)/3
print(avg(10, 20, 14))


# mainly it is used to pass a function as the argument of another function
def appl(fx, value):
  return 6 + fx(value)

print(appl(lambda x: x * x , 2))
