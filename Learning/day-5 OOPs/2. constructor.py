# A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

# A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.

class Person:   # class define

  def __init__(self, name, occ = "CA"):   # definining constructor by default done usnig __init__
    print("Hey I am a person")     # it will be automatically passed whenever we create a object.
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")

# here even before performing other iw will execute all automatically when we are making objects.

a = Person("Harry", "Developer")          # only 2 arguments as self is automatically passed as the object name
b = Person("Divya", "HR") 
c = Person("Debjeet")
a.info()
b.info()
c.info()
