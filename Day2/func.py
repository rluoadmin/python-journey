# functions
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))  # Output: Hello, Alice!


def greet(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"


print(greet("Alice", "Smith"))  # Output: Hello, Alice Smith!
print(greet(last_name="Smith", first_name="Alice"))  # Output: Hello, Alice Smith!


def greet(first_name, last_name="Doe"):
    return f"Hello, {first_name} {last_name}!"


import math
from math import pi, sqrt


def quadratic(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None  # No real roots
    root1 = (-b + sqrt(discriminant)) / (2 * a)
    root2 = (-b - sqrt(discriminant)) / (2 * a)
    return root1, root2


print("quadratic(1, -3, 2) = ", quadratic(1, -3, 2))  # Output: (2.0, 1.0)


def add_end(L=[]):
    L.append("END")
    return L


add_end()
add_end()
add_end()
