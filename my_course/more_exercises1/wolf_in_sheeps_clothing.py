animals = [animal for animal in input().split(", ")]
number_of_sheep = 0

if animals[-1] == "wolf":
    print("Please go away and stop eating my sheep")

else:
    for wolf in reversed(animals):
        if wolf != "wolf":
            number_of_sheep += 1
        else:
            print(f"Oi! Sheep number {number_of_sheep}! You are about to be eaten by a wolf!")