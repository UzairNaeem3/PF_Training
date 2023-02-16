def students():
    while True:
        total_students = input("Enter the total number of students in the class: ")
        math_students = input("Enter the number of students with Mathematics: ")
        bio_students = input("Enter the number of students with Bio: ")

        if total_students.isdigit() and math_students.isdigit() and bio_students.isdigit():
            total_students = int(total_students)
            math_students = int(math_students)
            bio_students = int(bio_students)
        else:
            print("Please enter the information in digits, Thank You!\n")
            continue

        if math_students + bio_students > total_students:
            print("Total students must be equal to or greater than math and bio students, Please correct it. Thank You!\n")
        else:
            math_bio_students = math_students + bio_students
            print("Number of students with Math & Bio: " + str(math_bio_students))
            not_math_bio_students = total_students - math_bio_students
            print("Number of students without Math & Bio: " + str(not_math_bio_students))
            break

students()