from math import ceil

budget = float(input())
flour_price = float(input())

pack_of_eggs_price = flour_price * 0.75
milk_liter_price = flour_price + (flour_price * 0.25)

loaf = pack_of_eggs_price + flour_price + (milk_liter_price / 4)

loaves_made = ceil(budget // loaf)

colored_eggs = loaves_made * 3

for i in range(1, loaves_made +1, +1):
    if i % 3 == 0:
        colored_eggs -= i - 2

budget_sum = budget - loaf * loaves_made

print(f"You made {loaves_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget_sum:.2f}BGN left.")