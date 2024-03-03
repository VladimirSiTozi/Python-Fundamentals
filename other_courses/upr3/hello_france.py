ticket_to_France = 150
type_price = input().split("|")
budget = float(input())
stared_budget = budget
separted = []
sumed = 0

for clothes in type_price:
        x = clothes.split("->")
        if x[0] == "Clothes":
            if float(x[1]) > 50 or float(x[1]) > budget:
                continue
            else:
                budget -= float(x[1])
                item_clothes = round(float(x[1]) + (float(x[1]) * 0.4), 2)
                sumed += item_clothes
                item_clothes = str(item_clothes)
                separted.append(item_clothes)

        elif x[0] == "Shoes":
            if float(x[1]) > 35 or float(x[1]) > budget:
                continue
            else:
                budget -= float(x[1])
                item_shoes = round(float(x[1]) + (float(x[1]) * 0.4), 2)
                sumed += item_shoes
                item_shoes = str(item_shoes)
                separted.append(item_shoes)


        elif x[0] == "Accessories":
            if float(x[1]) > 35 or float(x[1]) > budget:
                continue
            else:
                budget -= float(x[1])
                item_accessories = round(float(x[1]) + (float(x[1]) * 0.4), 2)
                sumed += item_accessories
                item_accessories = str(item_accessories)
                separted.append(item_accessories)


print("Every item sold price: ", end="")
print(", ".join(separted))
print(f"Sum of the sold prices {sumed}")
print(f"Left in my budget: {budget:.2f}")

sumed += budget
profit = sumed - stared_budget

print(f"Profit: {profit:.2f}")
print("Money earned + my money left in the budget: ", end="")
print(sumed)

if sumed >= ticket_to_France:
    print(f"Hello, France!")
else:
    print("Not enough money.")