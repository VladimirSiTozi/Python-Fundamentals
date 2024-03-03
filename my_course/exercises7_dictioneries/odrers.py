products = {'product': [], 'price': [], 'quantity': [], 'total': []}

while True:
    current_product = input()
    if current_product == 'buy':
        break

    name, str_price, str_quantity = current_product.split()
    price = float(str_price)
    quantity = int(str_quantity)

    if name in products['product']:
        products['quantity'] += quantity
    else:
        products['product'].append(name)
        products['price'].append(price)
        products['quantity'].append(quantity)

    total_for_the_product = round(price * quantity)
    products['total'].append(total_for_the_product)
    print(type(total_for_the_product))

for index in range(len(products)):
    print(f"{products['product'][index]} -> {products['total'][index]:.2f}")