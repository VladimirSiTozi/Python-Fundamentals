events = input().split("|") # first split
total_coins = 100
total_energy = 100
factory_is_open = True

for command in events:
    command_item = command.split("-") # second split
    type_of_command = command_item[0]
    value_of_command = int(command_item[1])
    if type_of_command == "rest":
        current_energy = total_energy
        total_energy += value_of_command
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_command == "order":
        if total_energy >= 30:
            print(f"You earned {value_of_command} coins.")
            total_coins += value_of_command
            total_energy -= 30
        else:
            total_energy += 50
            print("You had to rest!")

    else:
        if total_coins >= value_of_command:
            total_coins -= value_of_command
            print(f"You bought {type_of_command}.")
        else:
            print(f"Closed! Cannot afford {type_of_command}.")
            factory_is_open = False
            break
if factory_is_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")