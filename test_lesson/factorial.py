def factorial(n):
    if n < 0:
        raise ValueError("n should be > 0")

    if n in (1, 0):
        return 1

    return n * factorial(n - 1)
