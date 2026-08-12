def outer():
    n = 10

    def inner(y):
        nonlocal n
        n += y
        return n

    return inner


f = outer()
print(f(5))  # Output: 15
print(f(10))  # Output: 25
print(f(3))  # Output: 28
