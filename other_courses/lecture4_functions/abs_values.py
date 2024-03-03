numbers_as_string = input().split()
numbers = []

for numbers_as_string in numbers_as_string:
    numbers.append(abs(float(numbers_as_string)))

print(numbers)