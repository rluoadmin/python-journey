class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    count = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        Student.count += 1
        self.student_id = "2006" + str(Student.count)
        self.scores = {}

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")


class Manager:
    pass
