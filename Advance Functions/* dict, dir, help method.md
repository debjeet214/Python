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
```python
class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
```

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str




 
