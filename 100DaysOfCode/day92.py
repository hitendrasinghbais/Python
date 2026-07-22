#  function caching 
import time
from functools import lru_cache

@lru_cache (maxsize=None)
def fn(n):
    time.sleep(2)
    return n*10


print(fn(2))
print(fn(5))
print(fn(6))

print(fn(2))
print(fn(5))
print(fn(3))
