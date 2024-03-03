factor = int(input())
length = int(input())
multiples_list = []

for num in range(1, length + 1):
    number = num * factor
    multiples_list.append(number)

print(multiples_list)