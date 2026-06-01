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

# Created student objects with their name, email, and list of initial grades
student1 = Student('John', 'jbschoolname@gmail.com', [85, 90, 78])
student2 = Student('Jane', 'jaschoolname@gmail.com', [92, 88, 87])
student3 = Student('Tim', 'tdscoolname@gmail.com', [90, 95, 100])

# Add a new grade for each student
student1.add_grade(82)
student2.add_grade(91)
student3.add_grade(98)

# Display information about each student
student1.display_info()
student2.display_info()
student3.display_info()