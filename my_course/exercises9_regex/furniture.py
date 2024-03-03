import re


total_money = 0
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d+)!(\d+)'
bought_furnitures = []

while True:
    command = input()
    if command == 'Purchase':
        break

    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furnitures.append(furniture)
        total_money += float(price) * int(quantity)

print("Bought furniture:")
for furniture in bought_furnitures:
    print(furniture)
print(f"Total money spend: {total_money:.2f}")

# >>Sofa<<312.23!3
# >>TV<<300!5
# >Invalid<<!5
# Purchase
