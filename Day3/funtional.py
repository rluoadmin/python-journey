def add(a, b, f):
    return f(a) + f(b)


print(add(-5, 6, abs))  # Output: 11

# Map transforms each item, while Reduce combines multiple items into a single result.
names = ["adam", "LISA", "barT"]

result = list(map(str.capitalize, names))

print(result)
# ['Adam', 'Lisa', 'Bart']

from functools import reduce


def prod(numbers):
    return reduce(lambda x, y: x * y, numbers)


print(prod([2, 3, 4]))  # Output: 24


print(
    list(filter(lambda x: x % 2 == 1, range(1, 20)))
)  # Output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# decorators are a way to modify or enhance the behavior of functions or methods without changing their code. They are often used for logging, authentication, and other cross-cutting concerns.
import functools
from datetime import datetime


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s(): at %s" % (func.__name__, datetime.now()))
        return func(*args, **kw)

    return wrapper


@log
def add2(a, b, f):
    return f(a) + f(b)


print(add2(-5, 6, abs))  # Output: 11


int2 = functools.partial(int, base=2)
int2("1000000")
