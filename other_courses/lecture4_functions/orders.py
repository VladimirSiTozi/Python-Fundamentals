coffee = 1.50
water = 1.00
coke = 1.40
snacks = 2.00

product = input()
quantity = int(input())

def calculate(prod, quant):
    result = 0
    if prod == "coffee":
        result = coffee * quantity
    elif prod == "water":
        result = water * quantity
    elif prod == "coke":
        result = coke * quantity
    elif prod == "snacks":
        result = snacks * quantity
    return result


res = calculate(product, quantity)
print(f"{res:.2f}")
