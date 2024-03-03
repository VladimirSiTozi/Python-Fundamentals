number_of_order = int(input())
total = 0
total_sum = 0

for i in range(number_of_order):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())


    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules < 1 or capsules > 2000:
        continue

    total = price_per_capsule * days * capsules

    print(f"The price for the coffee is: ${total:.2f}")
    total_sum += total

    total = 0

print(f"Total: ${total_sum:.2f}")