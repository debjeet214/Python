# Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator. Here is an example of a simple class with a getter method:

class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value

obj = MyClass(10)
obj.value

# A setter updates the value of a variable, while a getter reads the value of a variable. A method that allows you to set or mutate the value of an attribute in a class. and both setter and getter is used to access the private values in the property of the class.

class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

obj = MyClass(10)
obj.value = 20
obj.value

