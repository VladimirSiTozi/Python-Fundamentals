def shoot(current_command, targets):
    command, index, power = current_command
    index = int(index)
    power = int(power)
    if 0 <= index <= len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.remove(targets[index])
    return targets


def add(current_command, targets):
    command, index, value = current_command
    index = int(index)
    value = int(value)
    if 0 <= index <= len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")
    return targets


def strike(current_command, targets):
    command, index, radius = current_command
    index = int(index)
    radius = int(radius)
    if 0 <= index - radius <= len(targets) and 0 <= index + radius <= len(targets):
        targets = targets[0: index - radius] + targets[index + radius + 1:]
    else:
        print("Strike missed!")
    return targets


target_values = [int(num) for num in input().split()]

while True:
    breaking_command = input()
    if breaking_command == "End":
        target_values = [str(x) for x in target_values]
        print('|'.join(target_values))
        break

    shooting = breaking_command.split()

    if shooting[0] == "Shoot":
        target_values = shoot(shooting, target_values)

    elif shooting[0] == "Add":
        target_values = add(shooting, target_values)

    elif shooting[0] == "Strike":
        target_values = strike(shooting, target_values)
