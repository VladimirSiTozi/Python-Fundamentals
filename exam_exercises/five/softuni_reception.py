employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
students = int(input())
students_passed = 0
hours = 0

while students_passed < students:
    hours += 1
    if hours % 4 == 0:
        continue
    students_passed += employee_one + employee_two + employee_three

print(f"Time needed: {hours}h.")