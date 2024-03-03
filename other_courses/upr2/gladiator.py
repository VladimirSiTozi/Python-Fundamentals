lost_fights_counter = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_broken = 0
sword_broken = 0
shield_broken = 0
armor_broken = 0

for fight in range(1, lost_fights_counter + 1):
    if fight % 2 == 0:
        helmet_broken += 1
    if fight % 3 == 0:
        sword_broken += 1
    if fight % 2 == 0 and fight % 3 == 0:
        shield_broken += 1
        if shield_broken % 2 == 0:
            armor_broken += 1

total_price = (helmet_price * helmet_broken) + (sword_price * sword_broken) + (shield_price * shield_broken) + \
              (armor_price * armor_broken)

print(f"Gladiator expenses: {total_price:.2f} aureus")