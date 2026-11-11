name = input("What is your name? ")
department = input("What is your department? ")
cgpa = float(input("What is your CGPA? "))
has_carryover = input("Do you have a carryover? True or False ")
has_carryover = has_carryover.lower() == "true"

first_course = input("What is your first course? ")
second_course = input("What is your second course? ")
third_course = input("What is your third course? ")

score_in_first_course = int(input(f"What is your score in {first_course}? "))
score_in_second_course = int(input(f"What is your score in {second_course}? "))
score_in_third_course = int(input(f"What is your score in {third_course}? "))

total_score = score_in_first_course + score_in_second_course + score_in_third_course
average_score = total_score / 3

if average_score > 100 or average_score < 0:
    print("Invalid score")
else:
    if average_score >= 70:
        grade = "A"
    elif average_score >= 60:
        grade = "B"
    elif average_score >= 50:
        grade = "C"
    elif average_score >= 45:
        grade = "D"
    else:
        grade = "F"

    print(f"Grade: {grade}")

    if average_score >= 50:
        if cgpa >= 4.5:
            if has_carryover:
                academic_standing = "Academic Review"
            else:
                academic_standing = "First Class Academic Standing"
        else:
            academic_standing = "General Academic Standing"

    else:
        academic_standing = "Academic Probation"

    print(f"Academic Standing: {academic_standing}")

    print("-------------------------------------------------------------------------------")
    print(               "STUDENT PERFORMANCE REPORT          ")
    print(f"Student: {name}")
    print(f"Department: {department}")
    print("Performance                                             Report")
    print(f"{first_course}                                                   {score_in_first_course}")
    print(f"{second_course}                                              {score_in_second_course}")
    print(f"{third_course}                                              {score_in_third_course}")
    print(f"Total                                                     {total_score}")
    print(f"Average Score:                                            {average_score}")
    print(f"Grade:                                                    {grade}")

    print("-------------------------------------------------------------------------------")
    print("Academic Status")
    print(f"Academic Standing:                                      {academic_standing}")
    print("-------------------------------------------------------------------------------")