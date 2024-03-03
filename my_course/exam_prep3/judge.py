all_student = {}
contest_list = []

while True:
    student = input()
    if student.startswith("no more time"):
        pass
        break

    current_student, contest, points = student.split(' -> ')

    if current_student not in all_student:
        all_student[current_student] = [{contest: int(points)}]
        if contest not in contest_list:
            contest_list.append(contest)

    else:
        if contest not in all_student[current_student]:
            all_student[current_student].append({contest: int(points)})
        else:
            if int(points) > all_student[current_student][contest]:
                all_student[current_student] = {contest: int(points)}

students_contests = {}
for student in all_student:
    print(student)
    for student in all_student[student]:
        print(all_student[student])