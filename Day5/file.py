file = open("input.txt", "r", encoding="utf-8")

# print(file.read())


while True:
    result = file.read(3)
    if not result:
        break
    print(result, end="")

file.close()

# with close automatically closes the file after the block of code is executed, even if an error occurs. This is a better practice than manually opening and closing files.
with open("input.txt", "r", encoding="utf-8") as file:
    while True:
        result = file.read(3)
        if not result:
            break
        print(result, end="")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def __enter__(self):
        print("Entering the context...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context...")


with Person("Alice", 30) as person:
    person.greet()
