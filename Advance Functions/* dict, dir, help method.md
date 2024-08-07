# dir() method
The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object. Example:

```python
x = [1, 2, 3]
print(dir(x))     # this returns all the methods available in the program
print(x.__add__)  # it has the power to tell what an specific method is used for.
```

# dict attribute:
The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection. Example:
```python
class Person:
     def __init__(self, name, age):
         self.name = name
         self.age = age

p = Person("John", 30)
p.__dict__
```

# help method
The help() method in Python is a built-in function that is used to display the documentation of modules, classes, functions, keywords, and other objects. It is a very useful tool for quickly getting information about Python objects, including their attributes, methods, and usage. means it tells about what is used for what purpose only.

```python
import math
help(math)

my_list = [1, 2, 3]
help(my_list)
```





 
