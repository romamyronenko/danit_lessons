"""
1 1 2 3 5 8 13
"""

from functools import lru_cache


def my_cache(func):
    global cache
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]
        cache[n] = func(n)

        return cache[n]

    return wrapper


@lru_cache(maxsize=3)
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(10))
print(fib(20))
print(fib(30))
print(fib(40))
print(fib(50))
print(fib(200))
