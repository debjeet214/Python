# Way 1
def decorator_func(func):
  def inner():
    print("Before")
    func()
    print("Bye for now!!")
    print("After")
  return inner

@decorator_func
def printing():
  print("Hello")
  print("How are you?")

printing()
