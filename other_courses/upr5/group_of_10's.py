from math import ceil

number_sequence = [int(num) for num in input().split(", ")]
max_value = max(number_sequence)
number_of_groups = int(max_value) // 10
number_of_groups = [i for i in range(number_of_groups)]


for number in number_sequence:
    if 0 < number <= 10:
        number_of_groups[0].append(number)
    elif 10 < number <= 20:
        number_of_groups[1].append(number)
    elif 20 < number <= 30:
        number_of_groups[2].append(number)
    elif 30 < number <= 40:
        number_of_groups[3].append(number)
    elif 40 < number <= 50:
        number_of_groups[4].append(number)

print(number_of_groups)

