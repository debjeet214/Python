### Python- Instance 
In Python, variables can be defined at the class level or at the instance level.

## Class Instance:
Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. For example, a class variable can be used to store the number of instances of a class that have been created.

``` Python
class MyClass:
    class_variable = 0
    
    def __init__(self):
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print(MyClass.class_variable)
        

obj1 = MyClass()
obj2 = MyClass()

obj1.print_class_variable() # Output: 2
obj2.print_class_variable() # Output: 2
```

## instance variable
Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class. For example, an instance variable can be used to store the name of an employee in a class that represents an employee.

``` python
class MyClass:
    def __init__(self, name):
        self.name = name
        
    def print_name(self):
        print(self.name)

obj1 = MyClass("John")
obj2 = MyClass("Jane")

obj1.print_name() # Output: John
obj2.print_name() # Output: Jane
```
