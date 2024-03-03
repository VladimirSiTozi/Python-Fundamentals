n = int(input())
special_word = input()
not_filtered_strings = []
filtered_strings = []

for _ in range(n):
    current_string = input()
    not_filtered_strings.append(current_string)
    if special_word in current_string:
        filtered_strings.append(current_string)

print(not_filtered_strings)
print(filtered_strings)
