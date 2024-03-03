n = int(input())
word = input()
all_strings = []
strings_containing_word = []

for _ in range(n):
    current_word = input()
    all_strings.append(current_word)

    if word in current_word:
        strings_containing_word.append(current_word)

print(all_strings)
print(strings_containing_word)