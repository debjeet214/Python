## Generators
In Python, generators are a type of iterable, like lists or tuples, but they allow for more efficient memory usage when working with large datasets. Instead of generating all the values at once and storing them in memory, generators produce values on the fly & yield one value at a time. A generator function returns a generator object, which can be used to generate the values one by one as you iterate over it.

### Creating a Generator
In Python, you can create a generator by using the yield statement in a function. The yield statement returns a value from the generator and suspends the execution of the function until the next value is requested. Here's an example:

```python
def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# Output:
# 0
# 1
# 2
# 3
# 4
```

### explanation :
As you can see, the generator function my_generator() returns a generator object, which can be used to generate the values in the range 0 to 4. The next() function is used to request the next value from the generator, and the generator resumes its execution until it encounters another yield statement or until it reaches the end of the function.

## Another way using For in looping
```python
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
for value in gen:
    print(value)
```
