# String
string = "my name is rluo"
string_two = "my name is rluo2"

full = string + " " + string_two

my_long_string = """
long name
is 
rluoooooo
"""

long_dash = "-" * 10

len(long_dash)

is_logged_in = True

is_logged_out = False

fstring = f"Hi there, {string}"

# if
temperature = 31
if temperature > 30:
    print("very hot")
elif temperature > 25:
    print("hot")
else:
    print("nice")

# for
for i in range(5):
    print(i)
# output: 0,1,2,3,4

for i in range(1, 6):
    print(i)
# output: 1,2,3,4,5

for i in range(1, 10, 2):
    print(i)
# output: 1,3,5,7,9

# list
my_list = [1, 2, 3, 4, 5]
print(my_list[-1])  # output: 5
print(my_list[0])  # output: 1

my_list.append(6)
print(my_list)  # output: [1, 2, 3, 4, 5, 6]
my_list.remove(3)
print(my_list)  # output: [1, 2, 4, 5, 6]
my_list.insert(2, 3)
print(my_list)  # output: [1, 2, 3, 4, 5, 6]

# dictionary
my_dict = {}

# Dictionary with data
person = {"name": "Alice", "age": 30, "city": "New York"}

# Different ways to create
scores = dict(math=95, english=87, science=92)

print(person["name"])  # Output: Alice
print(scores["math"])  # Output: 95
print(scores.get("history", "Not Found"))  # Output: Not Found

# Tuples
# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = 42  # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20


# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}

import func

func.greet("rluo")  # Output: Hello, rluo!

L = ["apple", "banana", "cherry"]
for fruit in L:
    print(f"hello, {fruit}")

n1 = 255
print(hex(n1))  # Output: 0xff
