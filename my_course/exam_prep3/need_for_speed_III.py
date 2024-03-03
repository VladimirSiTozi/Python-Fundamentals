def base_function(n_number_of_cars, my_cars):
    my_cars = initial_cars_function(n_number_of_cars, my_cars)
    modify_function(my_cars)


def initial_cars_function(number_of_cars, cars):
    for n in range(number_of_cars):
        current_car, mileage, fuel = input().split('|')
        cars[current_car] = {'Mileage': int(mileage), 'Fuel': int(fuel)}
    return cars


def modify_function(cars):
    while True:
        command = input()
        if command.startswith('Stop'):
            stop_function(cars)
            break
        elif command.startswith('Drive'):
            drive_function(cars, command)

        elif command.startswith('Refuel'):
            refuel_function(cars, command)

        elif command.startswith('Revert'):
            revert_function(cars, command)


def drive_function(current_car, current_command):
    action, car, distance, fuel = current_command.split(' : ')
    if current_car[car]['Fuel'] < int(fuel):
        print("Not enough fuel to make that ride")
    else:
        current_car[car]['Fuel'] -= int(fuel)
        current_car[car]['Mileage'] += int(distance)
        print(f"{car} driven for {distance} kilometers. {fuel} "
              f"liters of fuel consumed.")

    if current_car[car]['Mileage'] >= 100000:
        print(f"Time to sell the {car}!")
        del current_car[car]


def refuel_function(current_car, current_command):
    action, car, fuel = current_command.split(' : ')
    current_car[car]['Fuel'] += int(fuel)
    if current_car[car]['Fuel'] > 75:
        fuel_amount = (current_car[car]['Fuel'] - 75) - int(fuel)
        current_car[car]['Fuel'] = 75
        print(f"{car} refueled with {abs(fuel_amount)} liters")
    else:
        print(f"{car} refueled with {fuel} liters")


def revert_function(current_car, current_command):
    action, car, kilometer = current_command.split(' : ')
    current_car[car]['Mileage'] -= int(kilometer)
    if current_car[car]['Mileage'] < 10000:
        current_car[car]['Mileage'] = 10000
    else:
        print(f"{car} mileage decreased by {kilometer} kilometers")


def stop_function(all_cars):
    for car in all_cars:
        print(f"{car} -> Mileage: {all_cars[car]['Mileage']} kms, Fuel in the tank: {all_cars[car]['Fuel']} lt.")


my_cars = {}
n_number_of_cars = int(input())

base_function(n_number_of_cars, my_cars)

# test(input)
# 4
# Lamborghini Veneno|11111|74
# Bugatti Veyron|12345|67
# Koenigsegg CCXR|67890|12
# Aston Martin Valkryie|99900|50
# Drive : Koenigsegg CCXR : 382 : 82
# Drive : Aston Martin Valkryie : 99 : 23
# Drive : Aston Martin Valkryie : 2 : 1
# Refuel : Lamborghini Veneno : 40
# Revert : Bugatti Veyron : 2000
# Stop

# 3
# Audi A6|38000|62
# Mercedes CLS|11000|35
# Volkswagen Passat CC|45678|5
# Drive : Audi A6 : 543 : 47
# Drive : Mercedes CLS : 94 : 11
# Drive : Volkswagen Passat CC : 69 : 8
# Refuel : Audi A6 : 50
# Revert : Mercedes CLS : 500
# Revert : Audi A6 : 30000
# Stop
