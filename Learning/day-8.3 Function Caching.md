## Define
Function caching (also known as memoization) is a technique used to store the results of expensive function calls and reuse the cached result when the same inputs occur again but without doing the same computation. This can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently. But it only keeps the cache for a single program run time, if we re-run the program it'll remove the cache memory.

## Usecase:
In Python, function caching can be achieved using the functools.lru_cache decorator. The functools.lru_cache decorator is used to cache the results of a function so that you can reuse the results instead of recomputing them every time the function is called. Here's an example:

```python
import functools

@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(20))
# Output: 6765
```

As you can see, the functools.lru_cache decorator is used to cache the results of the fib function. The maxsize parameter is used to specify the maximum number of results to cache. If maxsize is set to None, the cache will have an unlimited size.
