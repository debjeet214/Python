#In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following 
# syntax => lambda arguments: expression.
# lamda is just the simple and short form of the normal defined functions but it is expressed in one line without defining them. here, only the argument and expressions have to be sent.

cirlce_area = lambda x, y = 3.14:x*x*y
print(type(cirlce_area))
print(cirlce_area( x = 5))
