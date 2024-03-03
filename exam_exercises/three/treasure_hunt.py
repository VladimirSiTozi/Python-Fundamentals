def loot(command_items, my_chests):
    for item in command_items[1::]:
        if item not in my_chests:
            my_chests.insert(0, item)
    return my_chests


def drop(command_items, my_chests):
    index = int(command_items[1])
    if index <= len(my_chests):
        item = my_chests[index]
        my_chests.pop(index)
        my_chests.append(item)
    return my_chests


def steal(command_items, my_chests):
    stolen_items = []
    index = int(command_items[1])
    for times in range(index):
        stolen_items.insert(0, my_chests[-1])
        my_chests.pop()
    print(", ".join(stolen_items))
    return my_chests


treasure_chest = [item for item in input().split("|")]

while True:
    break_command = input()
    if break_command == "Yohoho!":
        break
    command = break_command.split()
    if command[0] == "Loot":
        treasure_chest = loot(command, treasure_chest)

    elif command[0] == "Drop":
        treasure_chest = drop(command, treasure_chest)

    elif command[0] == "Steal":
        treasure_chest = steal(command, treasure_chest)

length = len("".join(treasure_chest))

if len(treasure_chest) > 0:
    pirate_credits = length / len(treasure_chest)
    print(f"Average treasure gain: {pirate_credits:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")