quantity = int(input())
days = int(input())

total_cost = 0
total_spirit = 0

for current_day in range(1, days + 1, +1):
    if current_day % 11 == 0:
        quantity += 2

    if current_day % 2 == 0:
        total_cost += quantity * 2
        total_spirit += 5

    if current_day % 3 == 0:
        total_cost += quantity * (5 + 3)
        total_spirit += 3 + 10

    if current_day % 5 == 0:
        total_cost += quantity * 15
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30

    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += 5 + 3 + 15

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")