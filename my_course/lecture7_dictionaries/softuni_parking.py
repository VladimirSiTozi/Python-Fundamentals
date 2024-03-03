parking_lot = {}
n_number_of_commands = int(input())

for _ in range(n_number_of_commands):
    current_command = input().split()

    if current_command[0] == "register":
        command, name, plate = current_command
        if name not in parking_lot:
            parking_lot[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_lot[name]}")

    elif current_command[0] == "unregister":
        command, name = current_command
        if name in parking_lot:
            parking_lot.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for owner, car_plate in parking_lot.items():
    print(f"{owner} => {car_plate}")

# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy

# 4
# register Jony AA4132BB
# register Jony AA4132BB
# register Linda AA9999BB
# unregister Jony
#
# 6
# register Jacob MM1111XX
# register Anthony AB1111XX
# unregister Jacob
# register Joshua DD1111XX
# unregister Lily
# register Samantha AA9999BB
