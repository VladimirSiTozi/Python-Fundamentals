first_string = input()
second_string = input()
last_printed = first_string

for char in range(len(first_string)):
    left_part = second_string[:char + 1]
    right_part = first_string[char + 1:]
    current_string = left_part + right_part

    if current_string == last_printed:
        continue
    print(current_string)
    last_printed = current_string