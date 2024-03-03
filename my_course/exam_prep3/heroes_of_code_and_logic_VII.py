def initial_heroes(n_of_heroes):
    initial_heroes_list = {}
    for n in range(int(n_of_heroes)):
        hero, HP, MP = input().split()
        HP = int(HP)
        MP = int(MP)

        if HP > 100:
            HP = 100
        if MP > 200:
            MP = 200

        initial_heroes_list[hero] = {'Health': HP, 'Mana': MP}
    return initial_heroes_list


def playing_the_game(initial_heroes_list):
    while True:
        command = input()
        if command.startswith('End'):
            end_of_game_func(initial_heroes_list)
            break

        elif command.startswith('CastSpell'):
            command = command.split(' - ')
            cast_spell_func(initial_heroes_list, command)

        elif command.startswith('TakeDamage'):
            command = command.split(' - ')
            take_damage_func(initial_heroes_list, command)

        elif command.startswith('Recharge'):
            command = command.split(' - ')
            recharge_func(initial_heroes_list, command)

        elif command.startswith('Heal'):
            command = command.split(' - ')
            heal_func(initial_heroes_list, command)


def cast_spell_func(initial_heroes_list, command):
    current_command, hero_name, mana, spell_name = command
    if initial_heroes_list[hero_name]['Mana'] >= int(mana):
        initial_heroes_list[hero_name]['Mana'] -= int(mana)
        print(f"{hero_name} has successfully cast {spell_name} and now has {initial_heroes_list[hero_name]['Mana']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")


def take_damage_func(initial_heroes_list, command):
    current_command, hero_name, damage, attacker = command
    initial_heroes_list[hero_name]['Health'] -= int(damage)
    if initial_heroes_list[hero_name]['Health'] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {initial_heroes_list[hero_name]['Health']}"
              f" HP left!")
    else:
        print(f"{hero_name} has been killed by {attacker}!")
        del initial_heroes_list[hero_name]


def recharge_func(initial_heroes_list, command):
    current_command, hero_name, amount = command
    initial_heroes_list[hero_name]['Mana'] += int(amount)
    if initial_heroes_list[hero_name]['Mana'] > 200:
        amount_recovered = (initial_heroes_list[hero_name]['Mana'] - 200) - int(amount)
        initial_heroes_list[hero_name]['Mana'] = 200
        print(f"{hero_name} recharged for {abs(amount_recovered)} MP!")
    else:
        print(f"{hero_name} recharged for {amount} MP!")


def heal_func(initial_heroes_list, command):
    current_command, hero_name, amount = command
    initial_heroes_list[hero_name]['Health'] += int(amount)
    if initial_heroes_list[hero_name]['Health'] > 100:
        amount_recovered = (initial_heroes_list[hero_name]['Health'] - 100) - int(amount)
        initial_heroes_list[hero_name]['Health'] = 100
        print(f"{hero_name} healed for {abs(amount_recovered)} HP!")
    else:
        print(f"{hero_name} healed for {amount} HP!")


def end_of_game_func(initial_heroes_list):
    for hero in initial_heroes_list:
        print(f'{hero}\n  HP: {initial_heroes_list[hero]["Health"]}\n  MP: {initial_heroes_list[hero]["Mana"]}')


n_of_heroes = input()
initial_heroes_list = initial_heroes(n_of_heroes)
playing_the_game(initial_heroes_list)

# test input
# 4
# Adela 90 150
# SirMullich 70 40
# Ivor 1 111
# Tyris 94 61
# Heal - SirMullich - 50
# Recharge - Adela - 100
# CastSpell - Tyris - 1000 - Fireball
# TakeDamage - Tyris - 99 - Fireball
# TakeDamage - Ivor - 3 - Mosquito
# End

# 4
# Adela 90 150
# SirMullich 70 40
# Ivor 1 111
# Tyris 94 61
# Heal - SirMullich - 50
# Recharge - Adela - 100
# CastSpell - Tyris - 1000 - Fireball
# TakeDamage - Tyris - 99 - Fireball
# TakeDamage - Ivor - 3 - Mosquito
# End