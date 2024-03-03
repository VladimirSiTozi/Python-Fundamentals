budget = int(input())

while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break

    if int(command) > budget:
        print(f"You went in overdraft!")
        break
    else:
        budget -= int(command)