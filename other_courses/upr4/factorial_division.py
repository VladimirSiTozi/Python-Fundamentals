def factorial_of_first_num(a, b):
    result = 1
    for x in range(1, a + 1):
        result = result * x

    return result / b


first_number = int(input())
second_number = int(input())

x = (factorial_of_first_num(first_number, second_number))
print(f"{x:.2f}")