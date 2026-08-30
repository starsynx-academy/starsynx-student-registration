# STARSYNX Student Registration System
# This program manages student registration records.
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

    # Validate required information
    if not student_id or not name or not email or not phone or not program:
        print("\nError: All fields are required.")
        return

    # Prevent duplicate Student IDs
    for student in students:
        if student["student_id"] == student_id:
            print("\nError: Student ID already exists.")
            return

    # Create a student record
    student = {
        "student_id": student_id,
        "name": name,
        "email": email,
        "phone": phone,
        "program": program
    }

<<<<<<< HEAD
    # Add the student record to the list
=======
>>>>>>> 83bd29f (Complete student registration system)
    students.append(student)

    print("\nStudent registered successfully!")


# Display all registered students
def view_students():
    print("\n--- Registered Students ---")

<<<<<<< HEAD
    # Check whether any students are registered
=======
>>>>>>> 83bd29f (Complete student registration system)
    if not students:
        print("No students registered.")
        return

<<<<<<< HEAD
    # Display each student record
=======
>>>>>>> 83bd29f (Complete student registration system)
    for student in students:
        print("\nStudent ID:", student["student_id"])
        print("Name:", student["name"])
        print("Email:", student["email"])
        print("Phone:", student["phone"])
        print("Program:", student["program"])
        print("----------------------------")


<<<<<<< HEAD
# Search for a student using Student ID
=======
# Search for a student
>>>>>>> 83bd29f (Complete student registration system)
def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID: ")

<<<<<<< HEAD
    # Search through all registered students
=======
>>>>>>> 83bd29f (Complete student registration system)
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


<<<<<<< HEAD
# Update an existing student's information
=======
# Update student information
>>>>>>> 83bd29f (Complete student registration system)
def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID: ")

<<<<<<< HEAD
    # Find the student
    for student in students:
        if student["student_id"] == student_id:

=======
    for student in students:
        if student["student_id"] == student_id:
>>>>>>> 83bd29f (Complete student registration system)
            print("\nEnter new student information.")

            name = input("Enter Full Name: ")
            email = input("Enter Email Address: ")
            phone = input("Enter Phone Number: ")
            program = input("Enter Program: ")

<<<<<<< HEAD
            # Validate updated information
=======
>>>>>>> 83bd29f (Complete student registration system)
            if not name or not email or not phone or not program:
                print("\nError: All fields are required.")
                return

<<<<<<< HEAD
            # Update student information
=======
>>>>>>> 83bd29f (Complete student registration system)
            student["name"] = name
            student["email"] = email
            student["phone"] = phone
            student["program"] = program

            print("\nStudent updated successfully!")
            return

    print("\nStudent not found.")


<<<<<<< HEAD
# Delete a student record
=======
# Delete a student
>>>>>>> 83bd29f (Complete student registration system)
def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ")

<<<<<<< HEAD
    # Find and remove the student
=======
>>>>>>> 83bd29f (Complete student registration system)
    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            print("\nStudent deleted successfully!")
            return

    print("\nStudent not found.")


<<<<<<< HEAD
# Display the main menu
=======
# Main menu
>>>>>>> 83bd29f (Complete student registration system)
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

<<<<<<< HEAD
        # Register a student
        if choice == "1":
            register_student()

        # View all students
        elif choice == "2":
            view_students()

        # Search for a student
        elif choice == "3":
            search_student()

        # Update student information
        elif choice == "4":
            update_student()

        # Delete a student
        elif choice == "5":
            delete_student()

        # Exit the program
=======
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

>>>>>>> 83bd29f (Complete student registration system)
        elif choice == "6":
            print("\nThank you for using the STARSYNX Student Registration System.")
            break

<<<<<<< HEAD
        # Handle invalid menu choices
=======
>>>>>>> 83bd29f (Complete student registration system)
        else:
            print("\nInvalid choice. Please select a number from 1 to 6.")


# Start the application
if __name__ == "__main__":
    main()
