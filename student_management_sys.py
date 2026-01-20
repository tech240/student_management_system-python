# =====================================================
# ශිෂ්‍ය කළමනාකරණ පද්ධතිය (Student Management System)
# -----------------------------------------------------
# මේ Python program එක භාවිතා කරලා
# 1. නව ශිෂ්‍යයෙකු add කරන්න
# 2. සියලුම ශිෂ්‍යයන් view කරන්න
# 3. ශිෂ්‍යයන්ගේ average marks ගණනය කරන්න
# 4. ශිෂ්‍යයෙකු delete කරන්න
# 5. Data JSON file එකකට save / load කරන්න
#
# මේක beginner level Python project එකක්
# =====================================================


# ----------------- Required Modules Import -----------------

import os # os module එක භාවිතා කරන්නේ file එකක් තියෙනවද කියලා check කරන්න
import json # json module එක භාවිතා කරන්නේ data file එකකට save / load කරන්න


# ----------------- Menu Display -----------------

print("-- Student Management System ---") # User ට menu එක පෙන්වනවා

print("1. Add student")
print("2. View students")
print("3. Calculate average marks")
print("4. Delete student")
print("5. Exit")


# ----------------- Student Class -----------------

class Student: # Student class එක ශිෂ්‍යයෙකු represent කරන object එකක්

    def __init__(self, name, age, marks): # __init__ කියන්නේ constructor එක Student object එක create වෙද්දි auto run වෙන function එක
        self.name = name # self.name කියන්නේ student ගේ නම store කරන variable එක
        self.age = age # self.age කියන්නේ student ගේ වයස store කරන variable එක
        self.marks = marks # self.marks කියන්නේ marks list එක (උදා: [60,70,80])

    def average(self): # මේ function එකෙන් student ගේ average marks ගණනය කරනවා
        return sum(self.marks) / len(self.marks)
        # sum(self.marks) → සියලු marks එකතු කරනවා
        # len(self.marks) → marks ගණන
        # average = total / count

    def info(self): # student ගේ details string එකක් විදිහට return කරන function එක
        return f"{self.name}, Age: {self.age}, Avg Marks: {self.average():.2f}"
        # :.2f කියන්නේ decimal places 2ක් පෙන්වන්න


# ----------------- Save Students to JSON File -----------------

def save_students(students, filename="students.json"):
    # මේ function එක students list එක JSON file එකකට save කරනවා
    data = [] # JSON file එකට write කරන්න data list එකක් create කරනවා
    for st in students: # students list එකේ තියෙන සෑම Student object එකක්ම loop කරනවා
        data.append({
            "name": st.name,
            "age": st.age,
            "marks": st.marks
        })
    # Student object එක dictionary එකක් කරලා list එකට add කරනවා

    with open(filename, "w") as f: # "w" mode → file එක write mode එකෙන් open කරනවා
        json.dump(data, f) # data list එක JSON file එකට save කරනවා


# ----------------- Load Students from JSON File -----------------

def load_students(filename="students.json"): # මේ function එක JSON file එකෙන් data load කරලා Student objects list එකක් return කරනවා

    students = [] # empty students list එකක් create කරනවා
    if os.path.exists(filename): # JSON file එක exist වෙනවද කියලා check කරනවා

        with open(filename, "r") as f: # "r" mode → file එක read mode එකෙන් open කරනවා
            data = json.load(f) # JSON file එකේ data Python list එකක් කරගන්නවා
            for item in data: # data list එකේ dictionary එකක් එකක් loop කරනවා
                students.append(
                    Student(item["name"], item["age"], item["marks"])
                )
                # dictionary data භාවිතා කරලා Student object එකක් create කරලා list එකට add කරනවා

    return students # students list එක return කරනවා


# ----------------- Program Start -----------------

students = load_students()
# Program එක start වෙද්දි JSON file එකේ තියෙන students load කරනවා


# ----------------- Main Loop -----------------

while True: # Program එක exit කරනකල් loop වෙනවා

    choice = input("Choose: ") # User ගෙන් option එක input ගන්නවා


    # -------- Add Student --------
    if choice == "1":

        name = input("Name: ") # Student නම input ගන්නවා
        age = int(input("Age: ")) # Student වයස integer එකක් විදිහට input ගන්නවා
        marks = input("Marks (comma separated): ") # Marks comma වලින් input ගන්නවා උදා: 60,70,80
        marks_list = [int(m) for m in marks.split(",")] # "60,70,80" → ["60","70","80"] → [60,70,80]
        students.append(Student(name, age, marks_list)) # New Student object එක students list එකට add කරනවා
        save_students(students) # Updated students list එක JSON file එකට save කරනවා
        print("Student added successfully.")


    # -------- View Students --------
    elif choice == "2":

        if not students: # students list එක empty නම්
            print("No students found.")

        else:
            for s in students: # students list එක loop කරනවා
                print(s.info()) # Student info display කරනවා


    # -------- Calculate Average Marks --------
    elif choice == "3":
        if not students:
            print("No students available.")

        else:
            for s in students:
                print(f"{s.name} Average: {s.average():.2f}") # Student name එකත් average marks එකත් print කරනවා


    # -------- Delete Student --------
    elif choice == "4":

        name = input("Enter student name to delete: ") # Delete කරන්න student name එක input ගන්නවා
        students = [s for s in students if s.name != name] # Input කරපු name එකට match වෙන student remove කරනවා
        save_students(students) # Updated list එක JSON file එකට save කරනවා
        print("Student deleted (if existed).")


    # -------- Exit Program --------
    elif choice == "5":
        print("Exiting program.")
        break # loop එක stop කරලා program එක exit කරනවා


    # -------- Invalid Option --------
    else:
        print("Invalid choice!") # Wrong option එකක් input කලොත් message එක පෙන්වනවා

