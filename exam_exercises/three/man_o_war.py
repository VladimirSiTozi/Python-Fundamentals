def status(pirateship, max_health_capacity):
    health_minimum = max_health_capacity * 0.2
    counter = 0
    for sections in pirateship:
        if int(sections) < health_minimum:
            counter += 1
    return counter


def repair(current_command, pirateship, max_health_capacity):
    index= int(current_command[1])
    health = int(current_command[2])
    if 0 <= index < len(pirateship):
        pirateship[index] = int(pirateship[index])
        pirateship[index] += health
        if pirateship[index] > max_health_capacity:
            pirateship[index] = max_health_capacity
    return pirateship


def defend(current_command, pirateship):
    start_index = int(current_command[1])
    end_index = int(current_command[2])
    damage = int(current_command[3])
    length = len(pirateship)
    if start_index >= 0 and start_index < end_index and end_index < length:
        for section in pirateship[start_index:end_index + 1]:
            section = int(section) - damage
            pirateship[start_index] = section
            start_index += 1

    return pirateship


def fire(current_command, warship):
    index = int(current_command[1])
    damage = int(current_command[2])
    if 0 <= index < len(warship):
        warship[index] = int(warship[index])
        warship[index] -= damage
    return warship


pirate_ship_status = [sect for sect in input().split(">")]
war_ship_status = [sect for sect in input().split(">")]
maximum_health_capacity = int(input())
red_flag = True

while True:
    word = input()
    if word == "Retire":
        break
    command = word.split()
    if command[0] == "Fire":
        war_ship_status = fire(command, war_ship_status)
        for section in war_ship_status:
            if int(section) <= 0:
                print("You won! The enemy ship has sunken.")
                red_flag = False
                break
        if red_flag == False:
            break

    elif command[0] == "Defend":
        pirate_ship_status = defend(command, pirate_ship_status)
        for section in pirate_ship_status:
            if int(section) <= 0:
                print("You lost! The pirate ship has sunken.")
                red_flag = False
                break
        if red_flag == False:
            break

    elif command[0] == "Repair":
        pirate_ship_status = repair(command, pirate_ship_status, maximum_health_capacity)

    elif command[0] == "Status":
        counter = status(pirate_ship_status, maximum_health_capacity)
        print(f"{counter} sections need repair.")


if red_flag:
    pirate_total_result = sum([int(nums) for nums in pirate_ship_status])
    print(f"Pirate ship status: {pirate_total_result}")
    war_ship_status = sum([int(nums) for nums in war_ship_status])
    print(f"Warship status: {war_ship_status}")