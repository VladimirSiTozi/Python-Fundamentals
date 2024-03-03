def ascii_func(start, end):
    result = ''
    for num in range(ord(start) + 1, ord(end)):
        result += f"{chr(num)} "
        
    return result


first_char = input()
second_char = input()

print(ascii_func(first_char, second_char))
