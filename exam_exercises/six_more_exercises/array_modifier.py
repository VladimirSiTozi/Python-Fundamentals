def swapping(current_command, my_array):
    index1, index2 = int(current_command[1]), int(current_command[2])
    my_array[index1], my_array[index2] = my_array[index2], my_array[index1]
    return my_array


def multiplying(current_command, my_array):
    index1, index2 = int(current_command[1]), int(current_command[2])
    product = my_array[index1] * my_array[index2]
    my_array[index1] = product
    return my_array


def decreasing(current_command, my_array):
    for index, element in enumerate(my_array):
        my_array[index] = element -1
    return my_array


array_values = [int(num) for num in input().split()]

while True:
    breaking_command = input()
    if breaking_command == "end":
        break

    command = breaking_command.split()

    if command[0] == "swap":
        array_values = swapping(command, array_values)

    elif command[0] == "multiply":
        array_values = multiplying(command, array_values)

    elif command[0] == "decrease":
        array_values = decreasing(command, array_values)

array_values = [str(el) for el in array_values]
print(", ".join(array_values))