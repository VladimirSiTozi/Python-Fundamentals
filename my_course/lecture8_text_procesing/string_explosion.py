string = input()

for index, char in enumerate(string[::-1]):
    if char == '>':
        explodion = index + 1
        print(string[:index])
        print(string[explodion:])
        string = string[:index] + string[explodion:]

print(string)