# student_management_system-python
import json
import os

# -------------------------------
# Student Class
# -------------------------------
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def info(self):
        return f"Student Name: {self.name}, Age: {self.age}, Avg Marks: {self.average():.2f}"

# -------------------------------
# File Functions
# -------------------------------
def save_students(students, filename="students.json"):
    data = []
    for s in students:
        data.append({
            "name": s.name,
            "age": s.age,
            "marks": s.marks
        })
    with open(filename, "w") as f:
        json.dump(data, f)


def load_students(filename="students.json"):
    students = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
            for item in data:
                students.append(
                    Student(item["name"], item["age"], item["marks"])
                )
    return students

# -------------------------------
# MAIN PROGRAM
# -------------------------------
students = load_students()

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add student")
    print("2. View students")
    print("3. Calculate average marks")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Choose one: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        marks = list(map(int, input("Enter marks (space separated): ").split(",")))
        students.append(Student(name, age, marks))
        save_students(students)
        print("Student added successfully.")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for st in students:
                print(st.info())

    elif choice == "3":
        if not students:
            print("No students found.")
        else:
            for st in students:
                print(f"{st.name}'s Average Marks: {st.average():.2f}")

    elif choice == "4":
        name = input("Enter student name to delete: ")
        students = [s for s in students if s.name != name]
        save_students(students)
        print("Student deleted successfully.")

    elif choice == "5":
        print("Exiting program 👋")
        break

    else:
        print("Invalid choice!")
