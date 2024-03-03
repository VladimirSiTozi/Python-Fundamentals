number_of_lines = int(input())
sum_liter = 0
water_tank_liters = 255
for i in range(number_of_lines):
    liters_of_water = int(input())
    if sum_liter + liters_of_water <= water_tank_liters:
        sum_liter += liters_of_water
    else:
        print("Insufficient capacity!")
        continue
print(sum_liter)