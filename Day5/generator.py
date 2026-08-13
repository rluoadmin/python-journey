class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __iter__(self):
        yield self.name
        yield self.age
        yield self.gender


P = Person("Alice", 30, "Female")
for attr in P:
    print(attr)
