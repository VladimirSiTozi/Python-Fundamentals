text = input()
numbers_list = []
strings_list = []

for symbol in text:
    if symbol in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        numbers_list.append(symbol)
    else:
        strings_list.append(symbol)

numbers_list = [int(x) for x in numbers_list]
take_list = []
skip_list = []

result = []

for index, value in enumerate(numbers_list):
    if index % 2 == 0:
        take_list.append(value)
    else:
        skip_list.append(value)

for take_num in take_list:
    for times in range(take_num):
        if not strings_list:
            break
        result.append(strings_list[0])
        strings_list.remove(strings_list[0])

    for skip_num in skip_list:
        for skip_times in range(skip_num):
            if not strings_list:
                break
            strings_list.remove(strings_list[0])
        skip_list.remove(skip_num)
        break

print(''.join(result))