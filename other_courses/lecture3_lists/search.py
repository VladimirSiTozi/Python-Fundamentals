number = int(input())
constant_word = input()

string = []
passed_strings = []

for word in range(number):
    current_string = input()
    string.append(current_string)
    if constant_word in current_string:
        passed_strings.append(current_string)
print(str(string))
print(passed_strings)