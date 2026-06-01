# Defined the Student class.
class Student:
    def __init__ (self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades

    # Methods for the Student class
    # Add a grade to the student's list of grades.
    def add_grade(self, grade):
        self.grades.append(grade)

    # Calculate the average grade for the student.
    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    # Display information about the student.
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade()}")

    # Return grades as a tuple and demonstrate immutability using try-except block.
    def grades_tuple(self):
        return tuple(self.grades)
    try:
        grades_tuple = grades_tuple()
        grades_tuple[0] = 100
    except TypeError as e:
        print(f"Error: {e} - Tuples are immutable, cannot modify grades.")
    
    

# Created student objects with their name, email, and list of initial grades.
student1 = Student('John', 'jbschoolname@gmail.com', [85, 90, 78])
student2 = Student('Jane', 'jaschoolname@gmail.com', [92, 88, 87])
student3 = Student('Tim', 'tdscoolname@gmail.com', [90, 95, 100])

# Add a new grade for each student.
student1.add_grade(82)
student2.add_grade(95)
student3.add_grade(98)

# Display information about each student.
student1.display_info()
student2.display_info()
student3.display_info()

# Create a dictionary to store students by their email for easy access.
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

# Retrieve a student by their email.
def get_student_by_email(email):
    return student_dict.get(email)

# Unique grades for all students
def unique_grades(student1, student2, student3):
    unique = {(set(student1.grades)).symmetric_difference(set(student2.grades)).symmetric_difference(set(student3.grades))}
    print(unique)

# Removed each students last grade using pop().
student1.grades.pop()
student2.grades.pop()
student3.grades.pop()

# Prints first and last grade for each student and the total number of grades. 
for student in [student1, student2, student3]:
    print(student.grades[0], student.grades[-1])
    print(len(student.grades))