print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in "ABC" for n in "XYZ"])

import os

print([d for d in os.listdir(".")])

print([x if x % 2 == 0 else -x for x in range(1, 11)])

"""
A generator allows us to generate values one at a time instead of storing all the values in memory at once. 
This makes it more memory-efficient, especially when dealing with large datasets or streams of data.

A generator produces values lazily, one at a time, which makes it memory-efficient.
"""
g = (x * x for x in range(1, 11) if x % 2 == 0)
for i in g:  # or call next(g) to get the next value from the generator
    print(i)
