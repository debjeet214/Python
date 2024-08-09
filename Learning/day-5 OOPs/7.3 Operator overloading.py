# OPerator overloading -- Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str.

class vector:
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k
  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"
  
# __add__ method is used here so that it can overload the + operator and get the expected outcome  
  def __add__(self, other):                     
    return vector(self.i + other.i, self.j + other.j, self.k + other.k)

v = vector(3, 7, 2)
print(v)

w = vector(1, 8, 6)
print(w)

print("Adding this two vector we get:")
# print(v+w)   # this will show error as first as python dont know how to use the + sign to add different vector components seperately

print(v+w)   # after defining __Add__ method we can do it
