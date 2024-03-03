def check_matches(index_one, index_two, my_sequence,):
    if my_sequence[index_one] == my_sequence[index_two]:
        if index_one < index_two:
            element = my_sequence.pop(index_two)
            my_sequence.pop(index_one)
        else:
            element = my_sequence.pop(index_one)
            my_sequence.pop(index_two)
        print(f"Congrats! You have found matching elements - {element}!")
    else:
        print("Try again!")
    return my_sequence


def not_match(my_sequence, total_moves):
    symbol_to_add = str(total_moves)
    middle = int(len(my_sequence) / 2)
    symbol_to_add = (f'-{symbol_to_add}a')
    my_sequence.insert(middle, symbol_to_add)
    my_sequence.insert(middle, symbol_to_add)
    print("Invalid input! Adding additional elements to the board")
    return my_sequence


sequence_of_elements = input().split()
moves = 0

while True:
    if not sequence_of_elements:
        print(f"You have won in {moves} turns!")
        break
    breaking_command = input()
    if breaking_command == "end":
        print("Sorry you lose :(")
        print(" ".join(sequence_of_elements))
        break
    command = breaking_command.split()
    index1, index2 = int(command[0]), int(command[1])
    moves += 1

    if index1 >= 0 and index2 >= 0 and index2 != index1:
        sequence_of_elements = check_matches(index1, index2, sequence_of_elements,)

    else:
        sequence_of_elements = not_match(sequence_of_elements, moves)