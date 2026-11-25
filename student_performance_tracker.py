students = []

next_student_number = 1

def generate_student_id():
    global next_student_number

    student_id = f"ST{next_student_number:03d}"
    next_student_number += 1

    return student_id

def add_student(students, name, score):
    student_id = generate_student_id()
    name = name.strip().title()
    students.append([student_id, name, score])
    print(f"{name} has been successfully added. Student ID: {student_id}")

def display_all_students(students):
    if students:
        for student in students:
            print(f"{student[0]} - {student[1]} - {student[2]}")
    else:
        print("No students registered")

def search_student(students, student_id):
    for student in students:
        if student[0].lower() == student_id.lower().strip():
            return f"Student ID: {student[0]}\nName: {student[1]}\nScore: {student[2]}"
    else:
        return "student not found"

def update_student_score(students, student_id, new_score):
    for student in students:
        if student[0].lower() == student_id.lower().strip():
            student[2] = new_score
            return f"{student[1]}'s score has been updated to {student[2]}"
    else:
        return "student not found"

def delete_student(students, student_id):
    for student in students:
        if student[0].lower() == student_id.lower().strip():
            students.remove(student)
            return f"{student[1]} ({student[0]}) has been deleted"
    else:
        return "student not found"

def calculate_statistics(students):
    if students:
        total_score = 0
        passed = 0
        for student in students:
            if student[2] >= 50:
                passed += 1
            total_score += student[2]

        average_score = round(total_score / len(students), 2)
        return average_score, passed, total_score
    else:
        return None

def find_highest_and_lowest_score(students):
    if students:
        highest_student = students[0][1]
        highest_id = students[0][0]
        highest_score = students[0][2]
        lowest_student = students[0][1]
        lowest_id = students[0][0]
        lowest_score = students[0][2]

        for student in students:
            if highest_score < student[2]:
                highest_score = student[2]
                highest_student = student[1]
                highest_id = student[0]

            if lowest_score > student[2]:
                lowest_score = student[2]
                lowest_student = student[1]
                lowest_id = student[0]

        return highest_student, highest_id, highest_score, lowest_student, lowest_id, lowest_score

    else:
        return None


def generate_class_report(students):
    statistics_result = calculate_statistics(students)
    if statistics_result is None:
        average_score = passed = total_score = "Unavailable"
    else:
        average_score, passed, total_score = statistics_result

    highest_lowest_result = find_highest_and_lowest_score(students)
    if highest_lowest_result is None:
        highest_student = highest_id = highest_score = lowest_student = lowest_id = lowest_score = "Unavailable"
    else:
        highest_student, highest_id, highest_score, lowest_student, lowest_id, lowest_score = highest_lowest_result

    return average_score, passed, total_score, highest_student, highest_id, highest_score, lowest_student, lowest_id, lowest_score

def display_class_report(students):
    average_score, passed, total_score, highest_student, highest_id, highest_score, lowest_student, lowest_id, lowest_score = generate_class_report(students)
    print(f"Average score: {average_score}")
    print(f"Passed: {passed}")
    print(f"Total score: {total_score}")
    print(f"Total students: {len(students)}")
    if highest_student == "Unavailable":
        print(f"Highest student: {highest_student}")
        print(f"Highest ID: {highest_id}")
        print(f"Highest score: {highest_score}")
        print(f"Lowest student: {lowest_student}")
        print(f"Lowest ID: {lowest_id}")
        print(f"Lowest score: {lowest_score}")
    else:
        print(f"{highest_student} ({highest_id}): {highest_score}")
        print(f"{lowest_student} ({lowest_id}): {lowest_score}")

print("===== STUDENT PERFORMANCE TRACKER =====")
while True:
    try:
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Update student score")
        print("5. Delete student")
        print("6. Generate class report")
        print("7. Exit")
        userchoice = int(input("Enter a choice: "))
        if userchoice == 1:
            while True:
                name = input("Enter a student's name: ").strip()

                if not name:
                    print("Name cannot be empty. Try again.")
                else:
                    break

            while True:
                try:
                    score = int(input("Enter a student's score: "))
                    if score < 0 or score > 100:
                        print("Must be between 0 and 100")
                    else:
                        break
                except ValueError:
                    print("Invalid input")
            add_student(students, name, score)
        elif userchoice == 2:
            display_all_students(students)
        elif userchoice == 3:
            student_id = input("Enter student ID: ")
            print(search_student(students, student_id))
        elif userchoice == 4:
            student_id = input("Enter student ID: ")
            while True:
                try:
                    new_score = int(input("Enter a student's new score: "))
                    if new_score < 0 or new_score > 100:
                        print("Must be between 0 and 100")
                    else:
                        break
                except ValueError:
                    print("Invalid input")
            print(update_student_score(students, student_id, new_score))
        elif userchoice == 5:
            student_id = input("Enter student ID: ")
            print(delete_student(students, student_id))
        elif userchoice == 6:
            display_class_report(students)
        elif userchoice == 7:
            print("Exited")
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input")