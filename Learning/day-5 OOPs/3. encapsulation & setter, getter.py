# encapsulation is used to restrict the access of private methods and variables within the class itself

# error code
class student:
  __name = "Debjeet"
st1 = student()
print(st1.__name)  # this will show error as private variable can not be accessed directly from outside.


# fixed code with the use of getter and setter methods to access the private variables
class student:
  __name = "Debjeet"
  def get_name(self):
    return self.__name
  def set_name(self, name):
    self.__name = name
  name = property(get_name, set_name)

st1 = student()
print(st1.name)
st1.name = "Divya"
print(st1.name)

# now it will be easily used.
