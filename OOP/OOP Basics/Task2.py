# Complete the following code according to the task in README.md.
# Don't change names of classes. Create names for the variables
# exactly the same as in the task.
class SchoolMember:
    def __init__(self, name, age) -> None:
        self.name = str(name)
        self.age = int(age)
    def show(self):
        message = f"Name: {self.name}, Age: {self.age}"
        return message

class Teacher(SchoolMember):
    def __init__(self, name, age, salary) -> None:
        super().__init__(name, age)
        self.salary = salary
    def show(self):
        return super().show() + f", Salary: {self.salary}"
        

class Student(SchoolMember):
    def __init__(self, name, age, grades) -> None:
        super().__init__(name, age)
        self.grades = grades
    def show(self):
        return super().show() + f", Grades: {self.grades}"
        


dr_evil = Teacher("Dr.Evil", 44, 5000)
fat_bastard = Student("Fat Bastard", 30, 10)
print(dr_evil.show())
print(fat_bastard.show())
