numbers = input().split(', ')
numb_ascii = {}

for string in numbers:
    if string not in numb_ascii:
        numb_ascii[string] = ord(string)

print(numb_ascii)

# characters = input().split(', ')
# char_dict = {char: ord(char) for char in characters}
#
# print(char_dict)