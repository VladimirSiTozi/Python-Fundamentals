def base_function(n_number_of_plants):
    my_entry_list = entry_plants(n_number_of_plants)
    modifying_function(my_entry_list)


def entry_plants(n_number_of_plants):
    for n in range(n_number_of_plants):
        plant, rarity = input().split('<->')
        my_plants_list[plant] = [rarity]
    return my_plants_list


def modifying_function(my_entry_list):

    while True:
        command = input()
        total = 0
        if command == 'Exhibition':
            print("Plants for the exhibition:")

            for key, value in my_entry_list.items():
                for rate in value[1:]:
                    int_rate = int(rate)
                    total += int_rate / (len(value) -1)
                print(f'- {key}; Rarity: {value[0]}; Rating: {total:.2f}')
                total = 0
            break

        command, params = command.split(': ')

        if command == 'Rate':
            plant, rating = params.split(' - ')
            rate_func(my_entry_list, plant, rating)

        elif command == 'Update':
            plant, new_rarity = params.split(' - ')
            rarity_function(my_entry_list, plant, new_rarity)

        elif command == 'Reset':
            remove_ratings(my_entry_list, params)


def rate_func(my_entry_list, plant, rating):
    if plant in my_entry_list:
        my_entry_list[plant].append(rating)
    else:
        print('error')


def rarity_function(my_entry_list, plant, new_rarity):
    if plant in my_entry_list:
        my_entry_list[plant][0] = new_rarity
    else:
        print('error')


def remove_ratings(my_entry_list, plant):
    if plant in my_entry_list:
        my_entry_list[plant] = my_entry_list[plant][0]
    else:
        print('error')


n_number_of_plants = int(input())
my_plants_list = {}

base_function(n_number_of_plants)


# 3
# Arnoldii<->4
# Woodii<->7
# Welwitschia<->2
# Rate: Woodii - 10
# Rate: Welwitschia - 7
# Rate: Arnoldii - 3
# Rate: Woodii - 5
# Update: Woodii - 5
# Reset: Arnoldii
# Exhibition
#
# 2
# Candelabra<->10
# Oahu<->10
# Rate: Oahu - 7
# Rate: Candelabra - 6
# Exhibition
