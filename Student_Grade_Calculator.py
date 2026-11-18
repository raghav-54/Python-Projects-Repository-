# ==============================================================================
# MCA 1st Semester Python Project: Student Grade Calculator & Management System
# Features: Nested Dictionaries, Functions, Error Handling, File Persistence (JSON), 
#           and ANSI Formatting for a clean Console GUI.
# ==============================================================================

import json
import os

DATA_FILE = "student_records.json"


def load_data():
    """Load student records from a JSON file for data persistence."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("\n[Warning] Data file is corrupted. Starting with an empty database.")
            return {}
    return {}


def save_data(records):
    """Save student records to a JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(records, file, indent=4)
    except IOError:
        print("\n[Error] Failed to save records to file.")


def calculate_grade(percentage):
    """Calculate grade using conditional statements (Unit III concept)."""
    if percentage >= 90:
        return "A+ (Outstanding)"
    elif percentage >= 80:
        return "A (Excellent)"
    elif percentage >= 70:
        return "B (Good)"
    elif percentage >= 60:
        return "C (Average)"
    elif percentage >= 40:
        return "D (Pass)"
    else:
        return "F (Fail)"


def add_student(records):
    """Add a new student record with validation and error handling."""
    print("\n" + "=" * 45)
    print("           ADD NEW STUDENT RECORD")
    print("=" * 45)
    
    roll_no = input("Enter Roll Number (e.g., MCA202601): ").strip()
    if not roll_no:
        print("\n[Error] Roll number cannot be empty.")
        return
    
    if roll_no in records:
        print(f"\n[Error] Student with Roll Number '{roll_no}' already exists.")
        return

    name = input("Enter Student Name: ").strip()
    if not name or not name.replace(" ", "").isalpha():
        print("\n[Error] Invalid name. Please use alphabetic characters only.")
        return

    # Taking marks for 3 core MCA 1st Sem subjects with robust error handling
    try:
        python_marks = float(input("Enter Python Programming Marks (0-100): "))
        dbms_marks = float(input("Enter Database Management Marks (0-100): "))
        maths_marks = float(input("Enter Discrete Mathematics Marks (0-100): "))
    except ValueError:
        print("\n[Error] Invalid input! Please enter numeric values for marks.")
        return

    # Validating range of marks
    if not (0 <= python_marks <= 100 and 0 <= dbms_marks <= 100 and 0 <= maths_marks <= 100):
        print("\n[Error] Marks must be between 0 and 100 for all subjects.")
        return

    total_marks = python_marks + dbms_marks + maths_marks
    percentage = total_marks / 3
    grade = calculate_grade(percentage)

    # Storing inside a nested dictionary (Unit II concept)
    records[roll_no] = {
        "name": name,
        "marks": {
            "Python Programming": python_marks,
            "Database Management": dbms_marks,
            "Discrete Mathematics": maths_marks,
        },
        "total": round(total_marks, 2),
        "percentage": round(percentage, 2),
        "grade": grade,
    }

    save_data(records)
    print(f"\n[Success] Student '{name}' added and saved successfully!")


def view_students(records):
    """Display all student records in a structured tabular format."""
    if not records:
        print("\n[Info] No student records found in database.")
        return

    print("\n" + "—" * 75)
    print(f"{'Roll No':<12} | {'Student Name':<20} | {'Total':<8} | {'Percentage':<10} | {'Grade':<15}")
    print("—" * 75)
    
    for roll_no, details in records.items():
        print(f"{roll_no:<12} | {details['name']:<20} | {details['total']:<8} | {details['percentage']:<10}% | {details['grade']:<15}")
    print("—" * 75)


def search_student(records):
    """Search for a specific student record by Roll Number."""
    if not records:
        print("\n[Info] Database is empty.")
        return
        
    roll_no = input("\nEnter Roll Number to search: ").strip()
    if roll_no in records:
        d = records[roll_no]
        print("\n" + "=" * 45)
        print(f"         STUDENT RECORD: {roll_no}")
        print("=" * 45)
        print(f"Name           : {d['name']}")
        print(f"Python Marks   : {d['marks']['Python Programming']}")
        print(f"DBMS Marks     : {d['marks']['Database Management']}")
        print(f"Maths Marks    : {d['marks']['Discrete Mathematics']}")
        print(f"Total Marks    : {d['total']} / 300")
        print(f"Percentage     : {d['percentage']}%")
        print(f"Final Grade    : {d['grade']}")
        print("=" * 45)
    else:
        print(f"\n[Error] No record found for Roll Number '{roll_no}'.")


def delete_student(records):
    """Delete a student record by Roll Number."""
    if not records:
        print("\n[Info] Database is empty.")
        return
        
    roll_no = input("\nEnter Roll Number to delete: ").strip()
    if roll_no in records:
        name = records[roll_no]["name"]
        del records[roll_no]
        save_data(records)
        print(f"\n[Success] Record for '{name}' (Roll No: {roll_no}) deleted successfully.")
    else:
        print(f"\n[Error] Student with Roll Number '{roll_no}' not found.")


def main():
    """Main program loop implementing menu-driven workflow."""
    student_records = load_data()

    while True:
        print("\n" + "=" * 45)
        print("     MCA 1ST SEM: STUDENT GRADE SYSTEM")
        print("=" * 45)
        print(" 1. Add New Student Record")
        print(" 2. View All Student Records")
        print(" 3. Search Student by Roll Number")
        print(" 4. Delete Student Record")
        print(" 5. Exit Program")
        print("=" * 45)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student(student_records)
        elif choice == "2":
            view_students(student_records)
        elif choice == "3":
            search_student(student_records)
        elif choice == "4":
            delete_student(student_records)
        elif choice == "5":
            print("\nThank you for using the Student Grade Calculator. Exiting...")
            break
        else:
            print("\n[Error] Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
