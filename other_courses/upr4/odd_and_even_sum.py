def even_or_odd(a):
    even = 0
    odd = 0
    for digit_as_str in numbers_as_str:
        digit = int(digit_as_str)

        if digit % 2 == 0:
            even += digit

        else:
            odd += digit

    return [even, odd]


numbers_as_str = input()

result = even_or_odd(numbers_as_str)
print(f"Odd sum = {result[1]}, Even sum = {result[0]}")


# def even_or_odd(a):
#     even = 0
#     odd = 0
#     for digit_as_str in numbers_as_str:
#         digit = int(digit_as_str)
#
#         if digit % 2 == 0:
#             even += digit
#
#         else:
#             odd += digit
#
#     return f"Odd sum = {odd}, Even sum = {even}"
#
#
# numbers_as_str = input()
# print(even_or_odd(numbers_as_str))





