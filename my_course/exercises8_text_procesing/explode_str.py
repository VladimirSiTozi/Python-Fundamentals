def explode_string(input_string):
    result = []
    i = 0

    while i < len(input_string):
        char = input_string[i]

        if char == '>':
            strength = int(input_string[i + 1])
            i += 2
            while i < len(input_string) and input_string[i] == '>':
                strength += int(input_string[i + 1])
                i += 2

            if result and strength > 0:
                result.pop()

            i -= 1  # Decrement i so that the current '>' is not skipped
        else:
            result.append(char)

        i += 1

    return ''.join(result)


if __name__ == "__main__":
    input_string = input("Enter the string: ")
    result = explode_string(input_string)
    print(result)