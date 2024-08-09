# FILE 1 --> emp.py
class Employee:   #  name of the class
  def __init__(self, name, id):   # constructor
    self.name = name
    self.id = id

  def __len__(self):              # to get the length of the object.
    i = 0
    for c in self.name:
      i = i + 1
    return i

  def __str__(self):              # this will print custom message instead of just telling it is object.
    return f"The name of the employee is {self.name} str"
    
  def __repr__(self):
    return f"Employee('{self.name}')"

  def __call__(self):              # whenever we use the object as function then, it will be called.
    print("Hey I am good")


# FILE 2 --> main.py    ( for calling all the defined methods)

from emp import Employee   # importing Employee class, from our  custom pakage emp

e = Employee("ranjani", 2200)

print(e)         # this will return the str method. it is used to showcase a object more precisely as we wanted.

print(repr(e))   # show repr only 

e()              # here the call method is ran as a function.
    # this e() returns whatever is in the call method. but if don't find the call method then it will show error as e() not callable then
