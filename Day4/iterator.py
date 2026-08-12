"""
An iterator allows us to access elements one at a time,
which is memory-efficient, especially for large datasets.
"""

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
it = iter(names)

print(next(it))  # Output: Alice
print(next(it))  # Output: Bob
print(next(it))  # Output: Charlie
print(next(it))  # Output: David
print(next(it))  # Output: Eve
print(next(it))  # Output: StopIteration


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __iter__(self):
        return PersonIterator(self)


class PersonIterator:
    def __init__(self, p):
        self.p = p
        self.index = 0
        self.attrs = [p.name, p.age, p.gender]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.attrs):
            current_attr = self.attrs[self.index]
            self.index += 1
            return current_attr
        else:
            raise StopIteration


p = Person("Alice", 30, "Female")
for attr in p:
    print(attr)


class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.n:
            current_value = self.a
            self.a, self.b = self.b, self.a + self.b
            self.index += 1
            return current_value
        else:
            raise StopIteration


# Example usage:
fib = Fibonacci(10)
for num in fib:
    print(num)
