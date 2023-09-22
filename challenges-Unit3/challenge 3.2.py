
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students


if __name__ == "__main__":
   
    students = [
        Student("Hardik", "C0033", 3.9),
        Student("Dhoni", "C0007", 3.4),
        Student("Virat", "C0018", 3.8),
        Student("Rohit", "D0045", 3.7),
    ]

    
    sorted_students = sort_students(students)

    
    for student in sorted_students:
        print(f"Name: {student.name}, \nRoll Number: {student.roll_number},\nCGPA: {student.cgpa}\n")
