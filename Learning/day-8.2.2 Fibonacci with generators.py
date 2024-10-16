# generator function 
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Create the generator object
fib_gen = fibonacci_generator()

# Print the first 10 Fibonacci numbers
for i in range(10):
    print(next(fib_gen))
