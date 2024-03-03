word = input()
listed = []
listed.append(word)

output_list = []

for i, el in enumerate(word):
    if chr(65) <= el <= chr(90):
        output_list.append(i)

print(output_list)