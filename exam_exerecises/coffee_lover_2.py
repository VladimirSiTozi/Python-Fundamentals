def reversing(my_coffee_in_stock):
    my_coffee_in_stock = list(reversed(my_coffee_in_stock))
    return my_coffee_in_stock


def including(current_command, my_coffee_in_stock):
    coffee = current_command[1]
    my_coffee_in_stock.append(coffee)
    return my_coffee_in_stock


def removing(current_command, my_coffee_in_stock):
    first_or_last, n_to_remove = current_command[1], int(current_command[2])
    if n_to_remove <= len(my_coffee_in_stock):
        for _ in range(n_to_remove):
            if first_or_last == "first":
                my_coffee_in_stock.remove(my_coffee_in_stock[0])
            elif first_or_last == "last":
                my_coffee_in_stock.pop()
    return my_coffee_in_stock


def preferring(current_command, my_coffee_in_stock):
    index_one, index_two = int(current_command[1]), int(current_command[2])
    if 0 <= index_one <= len(my_coffee_in_stock) and 0 <= index_one <= len(my_coffee_in_stock):
        my_coffee_in_stock[index_one], my_coffee_in_stock[index_two] = \
            my_coffee_in_stock[index_two], my_coffee_in_stock[index_one]
    return my_coffee_in_stock


coffee_in_stock = [type_of_coffee for type_of_coffee in input().split()]
n_of_commands = int(input())

for number in range(n_of_commands):
    command = input()

    if command == "Reverse":
        coffee_in_stock = reversing(coffee_in_stock)

    else:
        command = command.split()

        if command[0] == "Include":
            coffee_in_stock = including(command, coffee_in_stock)

        elif command[0] == "Remove":
            coffee_in_stock = removing(command, coffee_in_stock)

        elif command[0] == "Prefer":
            coffee_in_stock = preferring(command, coffee_in_stock)

print("Coffees:")
print(" ".join(coffee_in_stock))