# method overriding
# Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.


class A:
  def show(self):         # function in the class a 
    print("in A show")    # definition accordingly

class B(A):               # inherting from class A
  def show(self):         # same function redefined in class B
    print("in B show")    # has different inlines

a1 = B()
a1.show()                 # this will print definition from class B only

a2 = A()
a2.show()

# here according to the class, same method produce diffent outputs. This is called the function overriding.
