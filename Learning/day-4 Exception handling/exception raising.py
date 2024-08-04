class NonIntArgumentException(Exception):
    pass

def handleNonIntArguments(func):
    def wrapper(*args):
        try:
            # Check if all arguments are integers
            if not all(isinstance(arg, int) for arg in args):
                raise NonIntArgumentException("Arguments must be integers")
            return func(*args)
        except NonIntArgumentException as e:
            print("This is an error due to unacceptable type mistakes")
            print(e)
            return None
    return wrapper

@handleNonIntArguments
def add_numbers(*args):
    return sum(args)

# Example usage
print(add_numbers(1, 2, 'a'))  # This should print the error message and return None
print(float(add_numbers(1, 2, 3)))    # This should return 6
