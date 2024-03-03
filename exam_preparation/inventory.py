def giving_command(bring_command):
    if word[0] == "Collect":
        if word[1] not in my_items:
            my_items.append(word[1])

    elif word[0] == "Drop":
        if word[1] in my_items:
            my_items.remove(word[1])

    elif word[0] == "Combine Items":
        two_items = word[1].split(":")
        if two_items[0] in my_items:
            index = my_items.index(two_items[0])
            my_items.insert(index + 1, two_items[1])

    elif word[0] == "Renew":
        if word[1] in my_items:
            my_items.remove(word[1])
            my_items.append(word[1])


my_items = input().split(", ")

while True:
    command = input()

    if command == "Craft!":
        break
    else:
        word = command.split(" - ")

        giving_command(command)

        # if word[0] == "Collect":
        #     if word[1] not in my_items:
        #         my_items.append(word[1])
        #     else:
        #         continue
        #
        # elif word[0] == "Drop":
        #     if word[1] in my_items:
        #         my_items.remove(word[1])
        #     else:
        #         continue
        #
        # elif word[0] == "Combine Items":
        #     two_items = word[1].split(":")
        #     if two_items[0] in my_items:
        #         index = my_items.index(two_items[0])
        #         my_items.insert(index + 1, two_items[1])
        #     else:
        #         continue
        #
        # elif word[0] == "Renew":
        #     if word[1] in my_items:
        #         my_items.remove(word[1])
        #         my_items.append(word[1])

output = ', '.join(my_items)
print(output)


