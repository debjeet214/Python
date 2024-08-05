## Constructors:
In object-oriented programming, the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class. The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use.

### Class method as Alternative of constructors:  
However, there are times when you may want to create an object in a different way, or with different initial values, than what is provided by the default constructor. This is where class methods can be used as alternative constructors.
A class method belongs to the class rather than to an instance of the class. One common use case for class methods as alternative constructors is when you want to create an object from data that is stored in a different format, such as a string or a dictionary. 

1. When an object is stroed directly using values.  ex- employee("john", 10000)
2. When an object from data that is stored in a different format, such as a string or a dictionary. ex- employee("John-10000").

lets take an example to get : For example, consider a class named "Person" that has two attributes: "name" and "age". The default constructor for the class might look like this:

```python
class Person:
    def __init__(self, name, age):    # default constructor
        self.name = name
        self.age = age
```

But what if you want to create a Person object from a string that contains the person's name and age, separated by a comma? You can define a class method named "from_string" to do this:

```python
class Person:
    def __init__(self, name, age):    # default constructor
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):     # alternative way to create constructor
        name, age = string.split(',')    # this will assign value to class object directly by applying the condition
        return cls(name, int(age))

person = Person.from_string("John Doe, 30")   # this can used to add values
```

