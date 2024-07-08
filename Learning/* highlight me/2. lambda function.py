#In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:
syntax => lambda arguments: expression
# lamda is just the simple and short form of the normal defined functions but it is expressed in one line without defining them. here, only the argument and expressions ahs to be send.

# Example 1:
double = lambda x: x * 2
print(double(5))

# Example 2: area of circle = A = π r²

radius = int(input("Enter the radius of the circle: "))
C_area = 3.14 * radius * radius
print(C_area)
