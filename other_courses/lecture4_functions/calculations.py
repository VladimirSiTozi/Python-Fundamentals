def calculate(opera, num1, num2):
    result = 0
    if operator == "multiply":
        result = number1 * number2
    elif operator == "divide":
        result = number1 / number2
    elif operator == "add":
        result = number1 + number2
    elif operator == "subtract":
        result = number1 - number2

    return result


operator = input()
number1 = float(input())
number2 = float(input())

print(f"{calculate(operator,number1, number2):.0f}")
