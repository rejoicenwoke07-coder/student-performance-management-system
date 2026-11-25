# University Student Performance Management System

## Project Overview

The University Student Performance Management System is a console-based Python project developed in two versions.

- **Version 1.0:** Collects and processes one student's academic information, calculates scores, assigns grades, and determines academic standing.
- **Version 2.0:** Introduces a multi-student performance tracker that allows users to add, display, search, update, and delete student records, as well as generate class performance reports.

The project demonstrates the gradual development of Python programming skills through practical application, problem-solving, and the use of functions and data structures.

## Features

### Version 1.0 — Student Performance System

- Collects student name and department.
- Collects CGPA and carryover status.
- Accepts scores for three courses.
- Calculates total and average scores.
- Assigns grades based on the student's average.
- Determines academic standing using average score, CGPA, and carryover status.
- Displays a structured student performance report.

### Version 2.0 — Student Performance Tracker

- Adds multiple student records.
- Automatically generates a unique student ID for each student.
- Displays all registered students.
- Searches for students using their IDs.
- Updates student scores.
- Deletes student records.
- Generates class performance reports.
- Calculates class average, total score, and number of students who passed.
- Identifies students with the highest and lowest scores.
- Validates user input, including student names, scores, and menu choices.

## Technologies Used
- Python

## Python Concepts Practised

### Version 1.0

- Variables and data types
- User input and type conversion
- Arithmetic operators
- Comparison and logical operators
- Boolean values
- Conditional statements (`if`, `elif`, `else`)
- Nested conditional statements
- Formatted output using f-strings

### Version 2.0

- Lists and nested lists
- List methods (`append`, `remove`)
- List indexing and modification
- `for` and `while` loops
- Functions, parameters, and arguments
- Return statements and returned values
- Tuple unpacking
- Counters and accumulators
- String methods (`strip`, `lower`, `title`)
- Global variables
- Input validation
- Exception handling (`try`, `except`, `ValueError`)
- Conditional statements and logical operators
- Breaking a program into reusable functions

## Grading Criteria (Version 1.0)

| Average Score | Grade |
|---|---|
| 70–100 | A |
| 60–69 | B |
| 50–59 | C |
| 45–49 | D |
| 0–44 | F |

## Academic Standing Rules (Version 1.0)

- Passed with CGPA of 4.5 or above and no carryover: First Class Academic Standing.
- Passed with CGPA of 4.5 or above and a carryover: Academic Review.
- Passed with CGPA below 4.5: General Academic Standing.
- Failed: Academic Probation.

## How to Run the Project

1. Install Python.
2. Clone or download this repository.
3. Open the project folder in PyCharm or another Python IDE.

### Running Version 1.0

Run `student_performance_system.py` to use the original single-student performance system.

### Running Version 2.0

Run `student_performance_tracker.py` to use the multi-student performance tracker.

## Project Scope and Limitations

This project consists of two versions of a console-based Python application.

Version 1.0 processes one student's academic record at a time, while Version 2.0 supports managing multiple student records through a menu-driven interface.

Version 2.0 currently stores student records in memory, meaning all records are lost when the program exits. It does not yet use permanent file storage or a database.

Future improvements may include:
- Permanent data storage using files or databases.
- A graphical user interface.
- A web-based student management system.
- Additional academic performance analysis features.

## Author
Rejoice

## Project Status

- Version 1.0: Completed.
- Version 2.0: Completed.
