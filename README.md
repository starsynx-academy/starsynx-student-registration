# STARSYNX Student Registration System

## Project Overview

The STARSYNX Student Registration System is a mini software project developed as part of a Software Engineering practical.

The system demonstrates how a software project moves from requirements analysis and system design to development, testing, debugging, and documentation.

The application is a command-line based student management system developed using Python.

## Project Objectives

The main objectives of this project are:

* Register new students
* Store student information
* View all registered students
* Search for a student using Student ID
* Update student information
* Delete student records
* Validate required information
* Prevent duplicate Student IDs
* Handle invalid menu choices
* Demonstrate software testing and debugging

## Target Users

* Students
* System Administrators

## Main Features

### 1. Student Registration

Allows users to register a new student by entering:

* Student ID
* Full Name
* Email Address
* Phone Number
* Program

### 2. View Students

Displays all registered student records.

### 3. Search Student

Allows users to search for a student using their Student ID.

### 4. Update Student

Allows users to update the name, email, phone number, and program of an existing student.

### 5. Delete Student

Allows users to remove an existing student record using the Student ID.

### 6. Input Validation

The system checks that all required fields are completed before registering or updating a student.

### 7. Duplicate ID Prevention

The system prevents registration of multiple students using the same Student ID.

### 8. Error Handling

The system displays appropriate messages when:

* Required information is missing
* A Student ID already exists
* A student cannot be found
* An invalid menu option is selected

## Software Engineering Process

This project follows the following development process:

1. Requirements Analysis
2. System Design
3. Development
4. Testing
5. Debugging
6. Documentation

## Project Structure

```text
starsynx-student-registration/
│
├── design/
│   ├── system-flowchart.png
│   └── use-case-diagram.png
│
├── requirements/
│   ├── functional-requirements.md
│   └── non-functional-requirements.md
│
├── src/
│   └── student_registration.py
│
└── README.md
```

## Technologies

* Python
* Git
* GitHub
* Visual Studio Code / GitHub Codespaces

## How to Run

### Step 1: Open the Project

Open the project in Visual Studio Code, GitHub Codespaces, or a local terminal.

### Step 2: Open the Project Directory

Make sure the terminal is opened inside the project folder.

### Step 3: Run the Application

Use the following command:

```bash
python src/student_registration.py
```

## System Menu

When the program starts, the following menu is displayed:

```text
1. Register Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

## Testing

The following core features were tested successfully:

| Feature          | Status |
| ---------------- | ------ |
| Register Student | Passed |
| View Students    | Passed |
| Search Student   | Passed |
| Update Student   | Passed |
| Delete Student   | Passed |
| Exit System      | Passed |

## Design Documentation

The project includes:

* Use Case Diagram
* System Flowchart
* Functional Requirements
* Non-Functional Requirements

These documents demonstrate the analysis and design stages of the software development process.

## Project Status

**Completed**

The core student registration and record management functionality has been implemented and tested successfully.

## Author

STARSYNX Academy
