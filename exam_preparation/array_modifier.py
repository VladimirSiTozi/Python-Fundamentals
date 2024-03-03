array_numbers = [int(num) for num in input().split(" ")]

while True:
    word = input()
    if word == "end":
        break
    command = word.split(" ")

    if command[0] == "swap":
        index1, index2 = int(command[1]), int(command[2])
        array_numbers[index1], array_numbers[index2] = array_numbers[index2], array_numbers[index1]

    elif command[0] == "multiply":
        index1, index2 = int(command[1]), int(command[2])
        array_numbers[index1] *= array_numbers[index2]

    elif command[0] == "decrease":
        array_numbers = [element - 1 for element in array_numbers]

array_numbers = [str(num) for num in array_numbers]
print(", ".join(array_numbers))