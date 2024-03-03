def exchange(current_command, list_data):
    index = int(current_command[1]) + 1
    if index - 1 > len(list_data) and index -1 < 0:
        result = print("Invalid index")
    else:
        slice_one = list_data[0:index]
        slice_two = list_data[index::]
        result = slice_two + slice_one
    return result


def max_index(current_command, list_data):
    odd_or_even = current_command[1]
    if odd_or_even == "odd":
        result = (list_data.index(max(i for i in list_data if i % 2 != 0)))
    elif odd_or_even == "even":
        result = (list_data.index(max(i for i in list_data if i % 2 == 0)))
    return result


def min_index(current_command, list_data):
    odd_or_even = current_command[1]
    if odd_or_even == "odd":
        result = (list_data.index(min(i for i in list_data if i % 2 != 0)))
    elif odd_or_even == "even":
        result = (list_data.index(min(i for i in list_data if i % 2 == 0)))
    return result

data = [int(num) for num in input().split()]
while True:
    break_command = input()
    if break_command == "end":
        pass
        break
    else:
        command = break_command.split()

    if command[0] == "exchange":
        exchange(command, data)

    elif command[0] == "max":
        print(max_index(command, data))

    elif command[0] == "min":
        print(min_index(command, data))

    elif command[0] == "first":
        pass