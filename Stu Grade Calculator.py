# MCA 1st Semester Python Project: Student Grade Calculator
# Uses only core fundamentals, dictionaries, functions, and control flow.


def calculate_grade(percentage):
    """Calculate grade using conditional statements."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"


def add_student(records):
    """Add a new student to the dictionary."""
    print("\n--- Add New Student ---")
    roll_no = input("Enter Roll Number: ")

    if roll_no in records:
        print("Error: Student with this Roll Number already exists!")
        return

    name = input("Enter Student Name: ")

    # Taking marks for 3 subjects with error handling
    try:
        python_marks = float(input("Enter Python Marks (out of 100): "))
        dbms_marks = float(input("Enter DBMS Marks (out of 100): "))
        maths_marks = float(input("Enter Maths Marks (out of 100): "))
    except ValueError:
        print("Invalid input! Please enter numeric values for marks.")
        return

    # Validating range of marks
    if not (
        0 <= python_marks <= 100
        and 0 <= dbms_marks <= 100
        and 0 <= maths_marks <= 100
    ):
        print("Error: Marks should be between 0 and 100.")
        return

    total_marks = python_marks + dbms_marks + maths_marks
    percentage = total_marks / 3
    grade = calculate_grade(percentage)

    # Storing inside a nested dictionary
    records[roll_no] = {
        "name": name,
        "marks": {
            "Python": python_marks,
            "DBMS": dbms_marks,
            "Maths": maths_marks,
        },
        "total": total_marks,
        "percentage": round(percentage, 2),
        "grade": grade,
    }

    print(f"Success! Student {name} added successfully.")


def view_students(records):
    """Display all student records using loops."""
    if not records:
        print("\nNo student records found in memory!")
        return

    print("\n--- All Student Records ---")
    for roll_no, details in records.items():
        print(f"Roll No: {roll_no} | Name: {details['name']}")
        print(f"  Marks: {details['marks']}")
        print(
            f"  Total: {details['total']} | Percentage: {details['percentage']}% | Grade: {details['grade']}"
        )
        print("-" * 40)


def search_student(records):
    """Search for a specific student by Roll Number."""
    roll_no = input("\nEnter Roll Number to search: ")
    if roll_no in records:
        details = records[roll_no]
        print(f"\n--- Record Found ---")
        print(f"Name: {details['name']}")
        print(f"Subjects & Marks: {details['marks']}")
        print(f"Total Marks: {details['total']}")
        print(f"Percentage: {details['percentage']}%")
        print(f"Final Grade: {details['grade']}")
    else:
        print("Student not found!")


def main():
    """Main program loop using while and conditional statements."""
    # Dictionary to store all student data temporarily in memory
    student_records = {}

    while True:
        print("\n===============================")
        print(" STUDENT GRADE CALCULATOR")
        print("===============================")
        print("1. Add Student Record")
        print("2. View All Students")
        print("3. Search Student by Roll No")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(student_records)
        elif choice == "2":
            view_students(student_records)
        elif choice == "3":
            search_student(student_records)
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
