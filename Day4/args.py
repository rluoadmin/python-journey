def show_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


nums = [1, 2, 3]
person = {"name": "Alice", "age": 30}
show_info(*nums, **person)

rain = False

dinner = "takeout" if rain else "dine-in"
print("Dinner option:", dinner)

lambda_func = lambda x: x * 2  # anonymous function that doubles the input value
result = lambda_func(5)
print("Result:", result)


def calculate(func, a, b):
    return func(a, b)


print("Sum:", calculate(lambda x, y: x + y, 3, 4))
print("Product:", calculate(lambda x, y: x * y, 3, 4))

a = [10, 20, 30, 40, 50]
b = map(lambda x: x * 2, a)
print("List:", a)
print("List:", list(b))

c = filter(lambda x: x > 25, a)
print("Filtered List:", list(c))

from functools import reduce

result = reduce(lambda x, y: x + y, a)
print("Reduced Result:", result)

result2 = [num * 2 for num in a if num > 25]
print("List Comprehension:", result2)
