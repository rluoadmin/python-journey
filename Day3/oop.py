"""
In Python 3, all classes ultimately inherit from object.
object is the base class of all classes and provides common behaviors and methods to all Python objects.

Inheritance promotes code reuse and allows us to extend existing classes without rewriting common functionality.

Polymorphism allows different objects to be treated through the same interface while providing their own implementations.
It makes code more flexible, extensible, and reduces coupling.

A mixin is a small class designed to provide a specific behavior or capability to other classes through multiple inheritance,
rather than representing an “is-a” relationship.
"""


class Student:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value + "!!!"

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def print_score(self):
        print("%s: %s" % (self.__name, self.__score))


s1 = Student("Bob", 59)
s1.name = "Alice"
print(s1.name)


# An enum represents a fixed set of named constants.
# It improves code readability, consistency, and type safety, and avoids magic numbers or strings.
from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
