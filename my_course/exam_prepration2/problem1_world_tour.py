def add_stop(travel_locations, index, string):
    if int(index) < len(travel_locations):
        travel_locations = travel_locations[:int(index)] + string + travel_locations[int(index):]
    print(travel_locations)
    return travel_locations


def remove_stop(travel_locations, start_index, end_index):
    if int(start_index) < len(travel_locations) and int(end_index) < len(travel_locations):
        travel_locations = travel_locations[:int(start_index)] + travel_locations[int(end_index)+1:]
    print(travel_locations)
    return travel_locations


def switch_stop(travel_locations, old_string, new_string):
    if old_string in travel_locations:
        travel_locations = travel_locations.replace(old_string, new_string)
    print(travel_locations)
    return travel_locations

def base_functions(travel_locations):
    while True:
        command = input()
        if command.startswith('Travel'):
            print(f"Ready for world tour! Planned stops: {travel_locations}")
            break

        elif command.startswith('Add Stop'):
            current_command, index, string = command.split(':')
            travel_locations = add_stop(travel_locations,index, string)

        elif command.startswith('Remove Stop'):
            current_command, start_index, end_index = command.split(':')
            travel_locations = remove_stop(travel_locations, start_index, end_index)

        elif command.startswith('Switch'):
            current_command, old_string, new_string = command.split(':')
            travel_locations = switch_stop(travel_locations, old_string, new_string)


travel_locations = input()
base_functions(travel_locations)

# test input
# Hawai::Cyprys-Greece
# Add Stop:7:Rome
# Remove Stop:11:16
# Switch:Hawai:Bulgaria
# Travel

# Albania:Bulgaria:Cyprus:Deuchland
# Add Stop:3:Nigeria
# Remove Stop:4:8
# Switch:Albania: Azərbaycan
# Travel

