# mainly finally is used to execute a block of code at the end of the program in functions where no normal code can be executed after returning a value

def func1():
  try:
    list_val = [1, 65, -3, 0, 76, 21, 8, 1]
    x = int(input("Enter the index  whose value you want to get: "))
    print(list_val[x])
    return 1
  except IndexError:
    print("Index is out of range")
    return 2
  except Exception as e:
    print(e)
    return 3
  finally:
    print("This is finally block always no matter what in") # this finally block will still execute in functions too
  print("this will not execute ") # see this code will never be executed in the o/p in functions

printing = func1()
print(printing)
