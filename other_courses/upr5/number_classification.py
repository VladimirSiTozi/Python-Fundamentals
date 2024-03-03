def positive_numbers(number):
    positives = [num for num in number if int(num) >= 0]
    return positives


def negative_numbers(number):
    negative = [num for num in number if int(num) < 0]
    return negative


def even_numbers(number):
    evens = [num for num in number if int(num) % 2 == 0]
    return evens


def odd_numbers(number):
    odds = [num for num in number if int(num) % 2 != 0]
    return odds


numbers = input().split(", ")
print(f"Positive: {', '.join(positive_numbers(numbers))}")
print(f"Negative: {', '.join(negative_numbers(numbers))}")
print(f"Even: {', '.join(even_numbers(numbers))}")
print(f"Odd: {', '.join(odd_numbers(numbers))}")

# test input
# 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33
#
#
# 1, 2, 53, 2, 21