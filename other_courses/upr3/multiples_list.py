factor = int(input())
counter = int(input())

lst_of_numbers = []

for number in range(factor, counter +1):
    lst_of_numbers.append((number * factor))


print(lst_of_numbers)