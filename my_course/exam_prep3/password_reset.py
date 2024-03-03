def modify_function(my_string):
    while True:
        command = input()
        if command.startswith('Done'):
            done_function(my_string)
            break
        elif command.startswith('TakeOdd'):
            my_string = take_odd(my_string)

        elif command.startswith('Cut'):
            my_string = cut_function(my_string, command)

        elif command.startswith('Substitute'):
            my_string = substitute_function(my_string, command)


def take_odd(my_string):
    new_odd_string = ''
    for char in range(1, len(my_string), 2):
        new_odd_string += my_string[char]
    print(new_odd_string)
    return new_odd_string


def cut_function(my_string, command):
    action, index, length = command.split()
    my_string = my_string[:int(index)] + my_string[int(index) + int(length):]
    print(my_string)
    return my_string


def substitute_function(my_string, command):
    action, substring, substitute = command.split()
    if substring in my_string:
        my_string = my_string.replace(substring, substitute)
        print(my_string)
    else:
        print("Nothing to replace!")
    return my_string

def done_function(my_string):
    print(f"Your password is: {my_string}")


initial_string = input()
initial_string = modify_function(initial_string)
