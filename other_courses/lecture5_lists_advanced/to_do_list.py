command = input()
to_do_list = [0] * 10

while command != "End":
    index, action = command.split("-")
    index = int(index) - 1
    to_do_list[index] = action
    command = input()

sorted = [el for el in to_do_list if el != 0]
print(sorted)