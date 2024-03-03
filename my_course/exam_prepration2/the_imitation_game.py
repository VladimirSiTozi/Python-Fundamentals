def base_function(encrypted_message):

    while True:
        command = input()
        if command.startswith('Decode'):
            print(f'The decrypted message is: {encrypted_message}')
            break

        elif command.startswith('Move'):
            current_command, number_of_letters = command.split('|')
            encrypted_message = move_function(encrypted_message, number_of_letters)

        elif command.startswith('Insert'):
            current_command, index, value = command.split('|')
            encrypted_message = insert_function(encrypted_message, index, value)

        elif command.startswith('ChangeAll'):
            current_command, substring, replacement = command.split('|')
            encrypted_message = change_all_function(encrypted_message, substring, replacement)


def move_function(encrypted_message, number_of_letters):
    string_to_move = encrypted_message[:int(number_of_letters)]
    encrypted_message = encrypted_message[int(number_of_letters):] + string_to_move
    return encrypted_message


def insert_function(encrypted_message, index, value):
    encrypted_message = encrypted_message[:int(index)] + value + encrypted_message[int(index):]
    return encrypted_message


def change_all_function(encrypted_message, substring, replacement):
    encrypted_message = encrypted_message.replace(substring, replacement)
    return encrypted_message


encrypted_message = input()
base_function(encrypted_message)

# test inputs
# owyouh
# Move|2
# Move|3
# Insert|3|are
# Insert|9|?
# Decode
#
# zzHe
# ChangeAll|z|l
# Insert|2|o
# Move|3
# Decode
