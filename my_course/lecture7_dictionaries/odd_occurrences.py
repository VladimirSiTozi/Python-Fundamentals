words = input().split()
my_dict = {}

for word in words:
    lower_word = word.lower()
    if lower_word not in my_dict:
        my_dict[lower_word] = 0
    my_dict[lower_word] += 1

for k, v in my_dict.items():
    if v % 2 != 0:
        print(k, end=" ")