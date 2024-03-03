n = int(input())
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"
filtered_list = []

numbers = [int(input()) for _ in range(n)]

command = input()

for num in numbers:
    filtered_command = (
        (command == COMMAND_EVEN and num % 2 == 0)or
        (command == COMMAND_ODD and num % 2 != 0)or
        (command == COMMAND_NEGATIVE and num < 0)or
        (command == COMMAND_POSITIVE and num >= 0)
    )

    if filtered_command:
        filtered_list.append(num)

print(filtered_list)