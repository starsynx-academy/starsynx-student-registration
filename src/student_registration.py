# Store all registered students
students = []


# Register a new student
def register_student():
    print("\n--- Register Student ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Full Name: ")
    email = input("Enter Email Address: ")
    phone = input("Enter Phone Number: ")
    program = input("Enter Program: ")

    # Check if Student ID already exists
    for student in students:
        if student["student_id"] == student_id:
            print("Error: Student ID already exists.")
            return

    # Validate that all required fields are filled
    if not student_id or not name or not email or not phone or not program:
        print("Error: All fields are required.")
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
# View all registered students
def view_students():
    print("\n--- Registered Students ---")

    if not students:
        print("No students registered.")
        return

    for student in students:
        print(f"\nStudent ID: {student['student_id']}")
        print(f"Name: {student['name']}")
        print(f"Email: {student['email']}")
        print(f"Phone: {student['phone']}")
        print(f"Program: {student['program']}")
        print("----------------------------")


# Search for a student using Student ID
def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["student_id"] == student_id:
            print("\nStudent Found!")
            print(f"Student ID: {student['student_id']}")
            print(f"Name: {student['name']}")
            print(f"Email: {student['email']}")
            print(f"Phone: {student['phone']}")
            print(f"Program: {student['program']}")
            return

    print("Student not found.")


# Update student information
def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["student_id"] == student_id:
            print("\nEnter new information:")

            name = input("Enter Full Name: ")
            email = input("Enter Email Address: ")
            phone = input("Enter Phone Number: ")
            program = input("Enter Program: ")

            if not name or not email or not phone or not program:
                print("Error: All fields are required.")
                return

            student["name"] = name
            student["email"] = email
            student["phone"] = phone
            student["program"] = program

            print("\nStudent updated successfully!")
            return

    print("Student not found.")


# Delete a student
def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            print("\nStudent deleted successfully!")
            return

    print("Student not found.")


# Main menu of the application
def main():
    while True:
        print("\n==============================")
        print("STARSYNX Student Registration System")
        print("==============================")
        print("1. Register Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

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
            print("Thank you for using the STARSYNX Student Registration System.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the application
if __name__ == "__main__":
    main()
