# Partial function : A partial function in Python is a way to fix a certain number of arguments of a function and generate a new function with fewer arguments. This is done using the functools.partial function.
from functools import partial
def add(n1, n2, n3, n4, n5):
  return n1+n2+n3+n4+n5

add = partial(add, 10, 20, 30)   # partially assinging/fixing values to some arguments.
print(add(40, 50))   # other arguments are being just passed by default/user



# 1. Default arguments are static, defined at function creation. With partial, you can dynamically create new functions at runtime with specific parameters pre-defined.
def greet(name, message):
    return f"{message}, {name}!"

# Define a partial dynamically
morning_greet = partial(greet, message="Good morning")
evening_greet = partial(greet, message="Good evening")

print(morning_greet("Alice"))  # Output: Good morning, Alice!
print(evening_greet("Bob"))    # Output: Good evening, Bob!



# example 2
# 2. Partial functions enhance modularity by allowing the creation of specialized functions with specific configurations.
def log_message(level, message):
    print(f"[{level}] {message}")

# Specialized loggers
info_log = partial(log_message, level="INFO")
error_log = partial(log_message, level="ERROR")

# Call info_log with the message only, as level is already set
info_log(message="Application started.")  # Output: [INFO] Application started.
error_log(message="An error occurred!")   # Output: [ERROR] An error occurred.
