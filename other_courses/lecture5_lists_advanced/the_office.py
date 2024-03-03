employees_happiness = input().split()
factor = int(input())
employees_happiness_factored = [int(employee) * factor for (employee) in employees_happiness]
average_employees_happiness = sum(employees_happiness_factored) / len((employees_happiness_factored))
happy_employees = [employee for employee in employees_happiness_factored if employee >= average_employees_happiness]

if len(happy_employees) >= len(employees_happiness_factored) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness_factored)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness_factored)}. Employees are not happy!")

# test input
# 2 3 2 1 3 3
# 4
#
# 1 2 3 4 2 1
# 3