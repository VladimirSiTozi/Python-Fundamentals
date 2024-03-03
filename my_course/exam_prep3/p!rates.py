def initial_cities():
    cities = {}
    while True:
        command = input()
        if command.startswith('Sail'):
            break
        city, population, gold = command.split('||')
        if city not in cities:
            cities[city] = {'Population': int(population), 'Wealth': int(gold)}
        else:
            cities[city]['Population'] += int(population)
            cities[city]['Wealth'] += int(population)
    return cities


def modify_function(my_cities):
    while True:
        command = input()
        if command.startswith('End'):
            end_function(my_cities)
            break

        elif command.startswith('Plunder'):
            my_cities = plunder_function(my_cities, command)

        elif command.startswith('Prosper'):
            my_cities = prosper_function(my_cities, command)


def plunder_function(my_cities, command):
    action, town, people, gold = command.split('=>')
    my_cities[town]['Population'] -= int(people)
    my_cities[town]['Wealth'] -= int(gold)
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if my_cities[town]['Population'] <= 0:
        del my_cities[town]
        print(f"{town} has been wiped off the map!")
        return my_cities
    if my_cities[town]['Wealth'] <= 0:
        del my_cities[town]
        print(f"{town} has been wiped off the map!")
    return my_cities


def prosper_function(my_cities, command):
    action, town, gold = command.split('=>')
    if int(gold) < 0:
        print("Gold added cannot be a negative number!")
    else:
        my_cities[town]['Wealth'] += int(gold)
        print(f"{gold} gold added to the city treasury. {town} now has {my_cities[town]['Wealth']} gold.")
    return my_cities


def end_function(my_cities):
    if my_cities:
        print(f"Ahoy, Captain! There are {len(my_cities)} wealthy settlements to go to:")
        for city in my_cities:
            print(f"{city} -> Population: {my_cities[city]['Population']} citizens, "
                  f"Gold: {my_cities[city]['Wealth']} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


my_cities = initial_cities()
modify_function(my_cities)

