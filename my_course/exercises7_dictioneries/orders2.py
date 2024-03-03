products = {}

while True:
    current_product = input()
    if current_product == 'buy':
        break

    name, str_price, str_quantity = current_product.split()
    price = float(str_price)
    quantity = int(str_quantity)

    if name not in products.keys():
        products[name] = [price, quantity]
        continue

    products[name][1] += quantity
    products[name][0] = price

for product, total_price in products.items():
    total = total_price[0] * total_price[1]
    print(f"{product} -> {total:.2f}")

