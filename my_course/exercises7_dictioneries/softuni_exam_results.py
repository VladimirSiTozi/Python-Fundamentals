names = {}
submissions = {}

while True:
    command = input()
    if '-' in command:
        command = command.split('-')

    elif ' ' in command:
        command = command.split()
        if command[1] == 'finished':
            break

        if command[1] == 'banned':
            break

    username, language, points = command
    new_points = int(points)

    if username not in names:
        names[username] += new_points

    else: names[username] < new_points

    submissions[language] = 0
    submissions[language] += 1

print(names)
print(submissions)