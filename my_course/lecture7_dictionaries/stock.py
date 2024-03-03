stock_data = input().split()
stock = {}

for i in range(0, len(stock_data), 2):
    product = stock_data[i]
    quantity = stock_data[i + 1]
    stock[product] = quantity

product_to_search = input().split()

for food in product_to_search:
    if food in stock.keys():
        print(f"We have {stock[food]} of {food} left")
    else:
        print(f"Sorry, we don't have {food}")