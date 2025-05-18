class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}, Marks: {self.marks}")

# Function to display all students
def display_all_students(student_list):
    print("\n \tAll Students ")
    for student in student_list:
        student.display_info()

# Function to search for a student by roll number
def search_student_by_roll(student_list, roll_number):
    found = False
    for student in student_list:
        if student.roll_number == roll_number:
            print("\nStudent found:")
            student.display_info()
            found = True
            break
    if not found:
        print("\nStudent with given roll number not found.")

# Function to calculate average marks
def calculate_average_marks(student_list):
    total = 0
    for student in student_list:
        total += student.marks
    average = total / len(student_list)
    print(f"\nAverage Marks: {average:.2f}")

# Main program
try:
    # Pre-written students
    students = [
        Student("Arpit",7, 85),
        Student("Gupta", 6, 90),
        Student("Rishab", 11, 78),
        Student("Somnath", 10, 92)
    ]

    # Display all students
    display_all_students(students)

    # Take input to search
    roll_to_search = int(input("\nEnter roll number to search: "))
    search_student_by_roll(students, roll_to_search)

    # Calculate and display average marks
    calculate_average_marks(students)

except Exception as e:
    print(f"An error occurred: {e}")
