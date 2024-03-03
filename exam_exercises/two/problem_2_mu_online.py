def potion(your_health, heal):
    your_health += heal
    gained_heal = heal
    if your_health > 100:
        your_health = 100
        gained_heal = abs(((your_health + heal) - 100) + heal)
    return your_health, gained_heal


def chest(your_bitcoins, coins):
    your_bitcoins += coins

    return your_bitcoins


def monster(your_health, damage):
    your_health -= damage
    return your_health


health = 100
bitcoins = 0

rooms = input().split("|")
for room in rooms:
    command, value = room.split()
    value = int(value)

    if command == "potion":
        health, gained = potion(health, value)
        print(f"You healed for {gained} hp.\nCurrent health: {health} hp.")
    elif command == "chest":
        bitcoins = chest(bitcoins, value)
        print(f"You found {value} bitcoins.")
    else:
        health = monster(health,value)
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.\nBest room: {rooms.index(room) +1}")
            break

if health > 0:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")