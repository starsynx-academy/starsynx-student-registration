# STARSYNX Student Registration System
# This program manages student registration records.

students = []


# Register a new student
def register_student():
    print("\n--- Register Student ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Full Name: ")
    email = input("Enter Email Address: ")
    phone = input("Enter Phone Number: ")
    program = input("Enter Program: ")

    # Validate required information
    if not student_id or not name or not email or not phone or not program:
        print("\nError: All fields are required.")
        return

    # Prevent duplicate Student IDs
    for student in students:
        if student["student_id"] == student_id:
            print("\nError: Student ID already exists.")
            return

    # Create student record
    student = {
        "student_id": student_id,
        "name": name,
        "email": email,
        "phone": phone,
        "program": program
    }

    # Add student to the list
    students.append(student)

    print("\nStudent registered successfully!")


# Display all registered students
def view_students():
    print("\n--- Registered Students ---")

    if not students:
        print("No students registered.")
        return

    for student in students:
        print("\nStudent ID:", student["student_id"])
        print("Name:", student["name"])
        print("Email:", student["email"])
        print("Phone:", student["phone"])
        print("Program:", student["program"])
        print("----------------------------")


# Search for a student
def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["student_id"] == student_id:
            print("\nStudent Found!")
            print("Student ID:", student["student_id"])
            print("Name:", student["name"])
            print("Email:", student["email"])
            print("Phone:", student["phone"])
            print("Program:", student["program"])
            return

    print("\nStudent not found.")


# Update student information
def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["student_id"] == student_id:
            print("\nEnter new student information.")

            name = input("Enter Full Name: ")
            email = input("Enter Email Address: ")
            phone = input("Enter Phone Number: ")
            program = input("Enter Program: ")

            if not name or not email or not phone or not program:
                print("\nError: All fields are required.")
                return

            student["name"] = name
            student["email"] = email
            student["phone"] = phone
            student["program"] = program

            print("\nStudent updated successfully!")
            return

    print("\nStudent not found.")


# Delete a student
def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            print("\nStudent deleted successfully!")
            return

    print("\nStudent not found.")


# Main menu
def main():
    while True:
        print("\n========================================")
        print("   STARSYNX STUDENT REGISTRATION SYSTEM")
        print("========================================")
        print("1. Register Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("\nThank you for using the STARSYNX Student Registration System.")
            break

        else:
            print("\nInvalid choice. Please select a number from 1 to 6.")


# Start the application
if __name__ == "__main__":
    main()
