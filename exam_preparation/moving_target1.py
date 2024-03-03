def bring_command(command):
    while True:
        command = input()

        if command == "End":
            break

        command_given, index, power = command.split(" ")
        index = int(index)
        power = int(power)

        if command_given == "Shoot":
            if index <= len(sequence_of_targets):
                sequence_of_targets[index] -= power
            else:
                continue

            if sequence_of_targets[index] <= 0:
                sequence_of_targets.remove(sequence_of_targets[index])

        elif command_given == "Add":
            if index <= len(sequence_of_targets):
                sequence_of_targets.insert(index, sequence_of_targets[power])
            else:
                print("Invalid placement!")
                continue

        elif command_given == "Strike":
            pass


sequence_of_targets = [int(num) for num in input().split(" ")]

bring_command(sequence_of_targets)
