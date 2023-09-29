class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students


students = [
    Student("Alice", "101", 3.8),
    Student("Bob", "102", 3.9),
    Student("Charlie", "103", 3.5),
    Student("David", "104", 3.7)
]

sorted_students = sort_students(students)


for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
