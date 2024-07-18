# first make the name in uppercase

def decor1(name):
  def inner():
    return name().upper()
  return inner

# now split the name in two parts
def decor2(func):
  def inner():
    return func().split()
  return inner

# always maintain the required order or application of decoration
@decor2
@decor1
def name():
  name = input("Enter your name: ")
  surname = input("Enter your surname: ")
  full_name = name + " " + surname
  return full_name

name()
