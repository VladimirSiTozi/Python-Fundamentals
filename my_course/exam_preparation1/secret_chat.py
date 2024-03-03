def decrypt_message(message):
    while True:
        command = input()
        if command.startswith('Reveal'):
            print(f'You have a new text message: {message}')
            break

        elif command.startswith('InsertSpace'):
            type_of_command, index = command.split(':|:')
            message = message[0:int(index)] + " " + message[int(index):]
            print(message)

        elif command.startswith('Reverse'):
            type_of_command, substring = command.split(':|:')
            if substring in message:
                message = message.replace(substring, '', 1)
            else:
                print("error")
                continue
            message = message + substring[::-1]
            print(message)

        elif command.startswith('ChangeAll'):
            type_of_command, substring, replacement = command.split(':|:')
            if substring in message:
                message = message.replace(substring, replacement,)
            print(message)


concealed_message = input()
decrypt_message(concealed_message)


# test input

# Hiware?uiy
# ChangeAll:|:i:|:o
# Reverse:|:?uoy
# Reverse:|:jd
# InsertSpace:|:3
# InsertSpace:|:7
# Reveal

# heVVodar!gniV
# ChangeAll:|:V:|:l
# Reverse:|:!gnil
# InsertSpace:|:5
# Reveal