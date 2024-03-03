number_of_lines = int(input())

# constant value
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_POSITIVE = 'positive'
COMMAND_NEGATIVE = 'negative'

# accepted numbers from the user
numbers_lst = []

for _ in range(number_of_lines):
    current_number = int(input())
    numbers_lst.append(current_number)

command = input()

filtered_numbers = []

for number in numbers_lst:
    filter_passes = (
        (command == COMMAND_EVEN and number % 2 == 0) or
        (command == COMMAND_ODD and number % 2 != 0) or
        (command == COMMAND_NEGATIVE and number < 0) or
        (command == COMMAND_POSITIVE and number > 0)
    )
    # if it's true
    if filter_passes:
        filtered_numbers.append(number)

print(filtered_numbers)