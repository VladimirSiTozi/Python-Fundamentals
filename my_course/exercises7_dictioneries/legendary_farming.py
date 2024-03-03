items = {"shards": 0, "fragments": 0, "motes": 0}
win = False

while True:
    if win:
        break
    current_items = input().split()

    for index in range(0, len(current_items), 2):
        quantity = int(current_items[index])
        material = current_items[index + 1].lower()

        if material not in items:
            items[material] = 0
        items[material] += quantity

        if items["shards"] >= 250:
            win = True
            print("Shadowmourne obtained!")
            items["shards"] -= 250

        elif items["fragments"] >= 250:
            win = True
            print("Valanyr obtained!")
            items["fragments"] -= 250

        elif items["motes"] >= 250:
            win = True
            print("Dragonwrath obtained!")
            items["motes"] -= 250

        if win:
            break

for item, quantity in items.items():
    print(f"{item}: {quantity}")


# 3 Motes 5 stones 5 Shards
# 6 leathers 255 fragments 7 Shards

# 123 silver 6 shards 8 shards 5 motes
# 9 fangs 75 motes 103 MOTES 8 Shards
# 86 Motes 7 stones 19 silver
