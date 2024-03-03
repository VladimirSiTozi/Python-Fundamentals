number = int(input("Enter your number: ")) #bigger
numbers_lst = []

for i in range(number):
    word = input(f"Enter your {number - i} words: ")
    numbers_lst.append(word)
print(numbers_lst)

number2 = int(input(f"Enter smaller number, than the first one: ")) #smaller
for y in range(number2):
    word = input(f"Enter {number2 - y} of you previous words: ")
    numbers_lst.remove(word)
print(numbers_lst)