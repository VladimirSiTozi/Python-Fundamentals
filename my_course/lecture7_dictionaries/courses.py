courses = {}

while True:
    break_command = input()
    if break_command == "end":
        break

    course_name, student_name = break_command.split(" : ")

    if course_name not in courses:
        courses[course_name] = []

    courses[course_name].append(student_name)

for course, student in courses.items():
    print(f"{course}: {len(courses[course])}")
    for name in student:
        print(f"-- {name}")
