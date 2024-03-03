gifts_planed = input().split()
OutOfStock = []
Required = []
JustInCase = []

while True:
    command = input()
    if command == "No Money":
        break

    elif "Required" in command:
        Required = command.split()
        index = Required[2]
        index = int(index)
        if index <= len(gifts_planed):
            gifts_planed[index] = Required[1]

    elif "JustInCase" in command:
        JustInCase = command.split()
        last_word = JustInCase[1]
        gifts_planed[-1] = last_word

    elif "OutOfStock" in command:
        OutOfStock = command.split()
        word = OutOfStock[1]
        while word in gifts_planed:
            x = gifts_planed.index(word)
            x = int(x)
            gifts_planed[x] = "None"

for none in gifts_planed:
    if none == "None":
        gifts_planed.remove(none)

print(" ".join(gifts_planed))