def sum_of_all_numbers(numbs):
    return sum(numbs)


def min_number(numbs):
    return min(numbs)


def max_number(numbs):
    return max(numbs)


numbers = [int(num) for num in input().split()]

print(f"The minimum number is {min_number(numbers)}")
print(f"The maximum number is {max_number(numbers)}")
print(f"The sum number is: {sum_of_all_numbers(numbers)}")


