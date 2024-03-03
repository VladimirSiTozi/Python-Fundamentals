companies = {}

while True:
    current_command = input()

    if current_command == 'End':
        break

    current_command = current_command.split(" -> ")
    company_name, employee_id = current_command

    if company_name not in companies:
        companies[company_name] = []

    if employee_id in companies[company_name]:
        continue

    companies[company_name].append(employee_id)

for company, employees in companies.items():
    print(company)
    for employee in employees:
        print(f'-- {employee}')