import collections

contest_and_passwords = {}
users = {}

while True:
    command = input().split(":")
    if command[0] == "end of contests":
        break
    contest, password = command
    contest_and_passwords[contest] = password

while True:
    current_command = input().split("=>")
    if current_command[0] == "end of submissions":
        break
    contest, password, username, points = current_command
    points = int(points)

    if contest in contest_and_passwords.keys():
        if password in contest_and_passwords[contest]:
            if username not in users:
                users[username] = {}

            if contest in users[username].keys():
                if users[username][contest] < points:
                    users[username][contest] = points
                    continue
                continue
            users[username][contest] = points

current_score = 0
best_score = 0
best_score_user = ''

for user in users.keys():
    for keys, values in users[user].items():
        current_score += values
        if current_score > best_score:
            best_score = current_score
            best_score_user = user
    current_score = 0

print(f"Best candidate is {best_score_user} with total {best_score} points.")
print("Ranking:")

sorted_users = collections.OrderedDict(sorted(users.items()))

for user, subjects in sorted_users.items():
    print(user)
    for subject, score in subjects.items():
        print(f"# {subject} -> {score}")
