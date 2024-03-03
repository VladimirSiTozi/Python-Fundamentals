first_employee_per_hour = int(input())
second_employee_per_hour = int(input())
third_employee_per_hour = int(input())
number_of_students = int(input())
hours = 0

while number_of_students > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    else:
        total_clients_per_hour = first_employee_per_hour + second_employee_per_hour + third_employee_per_hour
        number_of_students -= total_clients_per_hour

print(f"Time needed: {hours}h.")