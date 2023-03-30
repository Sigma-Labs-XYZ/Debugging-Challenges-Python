def factorial(n: int) -> int:
    if n < 0:
        return 1
    return n * factorial(n - 1)


def c2():
    return factorial(5)
