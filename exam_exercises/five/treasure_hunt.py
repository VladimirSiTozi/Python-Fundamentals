def loot(current_command, my_chest):
    for items in current_command[1::]:
        if items in my_chest:
            continue
        else:
            my_chest.insert(0, items)
    return my_chest


def drop(current_command, my_chest):
    item_index = int(current_command[1])
    if item_index <= len(my_chest):
        drop_item = my_chest.pop(item_index)
        my_chest.append(drop_item)
    return my_chest


def steal(current_command, my_chest):
    stolen_items = []
    items_to_steal = int(current_command[1])
    for items in range(items_to_steal):
        item = my_chest.pop()
        stolen_items.append(item)
        if not my_chest:
            break
    print(', '.join(list(reversed(stolen_items))))
    return my_chest


initial_treasure_chest = [item for item in input().split("|")]

while True:
    breaking_command = input()
    if breaking_command == "Yohoho!":
        break

    command = breaking_command.split()
    if command[0] == "Loot":
        initial_treasure_chest = loot(command, initial_treasure_chest)

    elif command[0] == "Drop":
        initial_treasure_chest = drop(command, initial_treasure_chest)

    elif command[0] == "Steal":
        initial_treasure_chest = steal(command, initial_treasure_chest)

sum_of_items = 0
for item in initial_treasure_chest:
    sum_of_items += len(item)

if not initial_treasure_chest:
    print("Failed treasure hunt.")
else:
    treasure = sum_of_items / len(initial_treasure_chest)
    print(f"Average treasure gain: {treasure:.2f} pirate credits.")