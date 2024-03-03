def is_even(num):
    return num % 2 == 0


numbers = [int(num) for num in input().split()]

new_list_filtered_numbers = list(filter(is_even, numbers))
print(new_list_filtered_numbers)
