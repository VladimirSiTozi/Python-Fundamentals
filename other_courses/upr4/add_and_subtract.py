def sum_numbers(a, b):
    result = a + b
    return result


def subtract(a, b):
    result = a - b
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

result1 = sum_numbers(first_number, second_number)

result2 = subtract(result1, third_number)

print(result2)