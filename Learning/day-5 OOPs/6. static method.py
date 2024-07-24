''' Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.  '''

# ex 1.
class Math:
    @staticmethod
    def add(a, b):
        return a + b
result = Math.add(1, 2)
print(result) # Output: 3


# ex 2.
class Math:                 # creating the class
  def __init__(self, num):  # initializing the attribute num
    self.num = num

  def addtonum(self, n):    # seperate function to add a number to it
    self.num = self.num +n
    
  @staticmethod             # declearing the static method, so that self is not needed to be called. 
  def add(a, b):            # and it is seperate from the class instances.
      return a + b
    
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(Math.add(7, 2)) # two ways to call the static method
print(a.add(7, 2))
