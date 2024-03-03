def base_function(initial_string):
    while True:
        command = input()
        if command.startswith("End"):
            pass
            break
        elif command.startswith('Translate'):
            initial_string = translate_function(initial_string, command)
            print(initial_string)

        elif command.startswith('Includes'):
            includes_function(initial_string, command)

        elif command.startswith('Start'):
            start_function(initial_string, command)

        elif command.startswith('Lowercase'):
            initial_string = lowercase_function(initial_string, command)
            print(initial_string)

        elif command.startswith('FindIndex'):
            find_index_function(initial_string, command)

        elif command.startswith('Remove'):
            initial_string = remove_function(initial_string, command)
            print(initial_string)


def translate_function(initial_string, command):
    action, char, replacement = command.split()
    initial_string = initial_string.replace(char, replacement)
    return initial_string


def includes_function(initial_string, command):
    action, substring = command.split()
    if substring in initial_string:
        print("True")
    else:
        print("False")


def start_function(initial_string, command):
    action, substring = command.split()
    if initial_string.startswith(substring):
        print("True")
    else:
        print("False")


def lowercase_function(initial_string, command):
    initial_string = initial_string.lower()
    return initial_string


def find_index_function(initial_string, command):
    action, char = command.split()
    current_index = initial_string.rfind(char)
    print(current_index)


def remove_function(initial_string, command):
    action, start_index, count = command.split()
    initial_string = initial_string[:int(start_index)] + initial_string[int(start_index) + int(count):]
    return initial_string


initial_string = input()
base_function(initial_string)

# test input
# //Thi5 I5 MY 5trING!//
# Translate 5 s
# Includes string
# Start //This
# Lowercase
# FindIndex i
# Remove 0 10
# End
#
# *S0ftUni is the B3St Plac3**
# Translate 2 o
# Includes best
# t the
# Lowercase
# FindIndex p
# Remove 2 7
# End