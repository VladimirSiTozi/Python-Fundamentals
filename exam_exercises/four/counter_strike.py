initial_energy = int(input())
win_count = 0

while True:
    command = input()
    if command == "End of battle":
        print(f"Won battles: {win_count}. Energy left: {initial_energy}")
        break
    distance = int(command)

    initial_energy -= distance
    if initial_energy >= 0:
        win_count += 1
        if win_count % 3 == 0:
            initial_energy += win_count
    else:
        initial_energy = 0
        print(f"Not enough energy! Game ends with {win_count} won battles and {initial_energy} energy")
        break
