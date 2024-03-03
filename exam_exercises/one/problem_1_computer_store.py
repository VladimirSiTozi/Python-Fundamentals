total_price = 0
taxes = 0
special_price = 0

while True:
    customer = input()

    if customer == "special":
        special_price = (total_price + taxes) * 0.9
        if total_price == 0:
            print("Invalid order!")
            break

        print("Congratulations you've just bought a new computer!\n"
              f"Price without taxes: {total_price:.2f}$\n"
              f"Taxes: {taxes:.2f}$\n"
              "-----------\n"
              f"Total price: {special_price:.2f}$")
        break

    elif customer == "regular":
        if total_price == 0:
            print("Invalid order!")
            break

        print("Congratulations you've just bought a new computer!\n"
              f"Price without taxes: {total_price:.2f}$\n"
              f"Taxes: {taxes:.2f}$\n"
              "-----------\n"
              f"Total price: {(total_price + taxes):.2f}$")
        break

    price = float(customer)

    if price < 0:
        print("Invalid price!")
        continue

    total_price += price
    taxes += price * 0.2
