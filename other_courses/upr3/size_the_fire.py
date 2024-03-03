fire_variables = input().split("#")
water = int(input())
effort = 0
total_fire = 0

print("Cells:")
for types in fire_variables:
    x = types.split(" = ")
    type_of_fire = x[0]
    value_of_cell = int(x[1])

    if value_of_cell > water:
        continue

    if type_of_fire == "Low" and 0 < value_of_cell <= 50:
        water -= value_of_cell
        effort += value_of_cell * 0.25
        total_fire += value_of_cell
        print(f" - {value_of_cell}")

    elif type_of_fire == "Medium" and 50 < value_of_cell <= 80:
        water -= value_of_cell
        effort += value_of_cell * 0.25
        total_fire += value_of_cell
        print(f" - {value_of_cell}")

    elif type_of_fire == "High" and 80 < value_of_cell <= 125:
        water -= value_of_cell
        effort += value_of_cell * 0.25
        total_fire += value_of_cell
        print(f" - {value_of_cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")