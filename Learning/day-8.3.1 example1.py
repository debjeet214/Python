# importing library
from functools import lru_cache
import time
#decorators
@lru_cache(maxsize=None)
def heavy_computation(x):
    time.sleep(2)
    return x * 21

#function call
print(heavy_computation(5))
print(heavy_computation(7)) # this will calculate after waiting 2 second sleep
print(heavy_computation(5)) # but as the function had input 5, so it'll not stop this time and run
print(heavy_computation(9))
print(heavy_computation(12))
print(heavy_computation(52))
print(heavy_computation(15))
# The function had input 5 & 7, so it'll not stop this time and run for input 5, 7
print(heavy_computation(5))
print(heavy_computation(7))
print(heavy_computation(96))
