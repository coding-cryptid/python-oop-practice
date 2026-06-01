class Student:
    def __init__ (self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades

def add_grade(self, grade):
    self.grades.append(grade)

def average_grade(self):
    if len(self.grades) == 0:
        return 0
    return sum(self.grades) / len(self.grades)

def display_info(self):
    print(f"Name: {self.name}")
    print(f"Email: {self.email}")
    print(f"Grades: {self.grades}")
    print(f"Average Grade: {self.average_grade()}")