n_of_days = int(input())
n_of_players = int(input())
group_energy = float(input())
water_per_person = float(input())
food_per_person = float(input())

total_water = water_per_person * n_of_players * n_of_days
total_food = food_per_person * n_of_players * n_of_days

for days in range(1, n_of_days +1):
    energy_lost = float(input())
    group_energy -= energy_lost

    if group_energy <= 0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        break

    if days % 2 == 0:
        group_energy += group_energy * 0.05
        total_water -= total_water * 0.3

    if days % 3 == 0:
        total_food -= total_food / n_of_players
        group_energy += group_energy * 0.1

if group_energy > 0:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")