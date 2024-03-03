student_academy = {}
n_lines = int(input())

for _ in range(n_lines):
    student = input()
    grade = float(input())

    if student not in student_academy:
        student_academy[student] = []
    student_academy[student].append(grade)

for student in student_academy:
    average = sum(student_academy[student]) / len(student_academy[student])
    if average >= 4.50:
        print(f"{student} -> {average:.2f}")


# 5
# John
# 5.5
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5

# 5
# Amanda
# 3.5
# Amanda
# 4
# Rob
# 5.5
# Christian
# 5
# Robert
# 2