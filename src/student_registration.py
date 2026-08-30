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
