force_book = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    if ' | ' in command:
        command = command.split(' | ')
        force_side, force_user = command
        if force_side not in force_book:
            force_book[force_side] = []
            if force_user not in force_book.values():
                force_book[force_side].append(force_user)

    elif ' -> ' in command:
        command = command.split(' -> ')
        force_user, force_side = command

        for key, value in force_book.items():
            if force_user in value:
                force_book[key].remove(force_user)

        if force_user not in force_book:
            force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for forces, jedis in force_book.items():
    if len(force_book[forces]) == 0:
        continue
    print(f"Side: {forces}, Members: {len(force_book[forces])}")

    for jedis in force_book[forces]:
        print(f"! {jedis}")

# Lighter | Royal
# Darker | DCay
# Ivan Ivanov -> Lighter
# DCay -> Lighter
# Lumpawaroo
#
# Light | Peter
# Dark | Kim
# Light | Kim
# Lumpawaroo

