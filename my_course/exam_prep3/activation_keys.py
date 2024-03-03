def base_function(raw_activation_key):
    while True:
        command = input()
        if command.startswith('Generate'):
            print(f'Your activation key is: {raw_activation_key}')
            break

        elif command.startswith('Contains'):
            current_command, substring = command.split('>>>')
            contains_function(raw_activation_key, substring)

        elif command.startswith('Flip'):
            current_command, position, start_index, end_index = command.split('>>>')
            raw_activation_key = flip_function(raw_activation_key, position, start_index, end_index)

        elif command.startswith('Slice'):
            current_command, start_index, end_index = command.split('>>>')
            raw_activation_key = slice_function(raw_activation_key, start_index, end_index)


def contains_function(raw_activation_key, substring):
    if substring in raw_activation_key:
        print(f"{raw_activation_key} contains {substring}")
    else:
        print("Substring not found!")


def flip_function(raw_activation_key, position, start_index, end_index):
    if position == 'Upper':
        new_upper_string = (raw_activation_key[int(start_index):int(end_index)]).upper()
        raw_activation_key = raw_activation_key[:int(start_index)] + new_upper_string + \
                             raw_activation_key[int(end_index):]
        print(raw_activation_key)
        return raw_activation_key

    elif position == 'Lower':
        new_lower_string = (raw_activation_key[int(start_index):int(end_index)]).lower()
        raw_activation_key = raw_activation_key[:int(start_index)] + new_lower_string + \
                             raw_activation_key[int(end_index):]
        print(raw_activation_key)
        return raw_activation_key


def slice_function(raw_activation_key, start_index, end_index):
    raw_activation_key = raw_activation_key[:int(start_index)] + raw_activation_key[int(end_index):]
    print(raw_activation_key)
    return raw_activation_key


raw_activation_key = input()
base_function(raw_activation_key)

# test input
# abcdefghijklmnopqrstuvwxyz
# Slice>>>2>>>6
# Flip>>>Upper>>>3>>>14
# Flip>>>Lower>>>5>>>7
# Contains>>>def
# Contains>>>deF
# Generate

# 134softsf5ftuni2020rockz42
# Slice>>>3>>>7
# Contains>>>-rock
# Contains>>>-uniContains>>>-rocks
# Flip>>>Upper>>>2>>>8
# Flip>>>Lower>>>5>>>11
# Generate
