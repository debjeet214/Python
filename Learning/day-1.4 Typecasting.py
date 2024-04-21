# Typecasting : The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

'''Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

Two Types of Typecasting:

Explicit typecasting:
The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion. It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .'''

string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number # now we get both the values as integer 
print("The Sum of both the numbers is: ", sum)

''' Implicit type casting:
Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python. Python converts a smaller data type to a higher data type to prevent data loss. '''

# example 
a = 7
print(type(a))
b = 3.7
print(type(b))
c = a + b
print(c)   # answer will be 10.7
print(type(c))  # Python automatically converts c to float as it is a float addition
