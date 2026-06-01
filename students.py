# Define the Student class
class Student:
    def __init__ (self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades


# Methods for the Student class

# Add a grade to the student's list of grades
def add_grade(self, grade):
    self.grades.append(grade)

# Calculate the average grade for the student
def average_grade(self):
    if len(self.grades) == 0:
        return 0
    return sum(self.grades) / len(self.grades)

# Display information about the student
def display_info(self):
    print(f"Name: {self.name}")
    print(f"Email: {self.email}")
    print(f"Grades: {self.grades}")
    print(f"Average Grade: {self.average_grade()}")

