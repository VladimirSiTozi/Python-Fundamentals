days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
wealth = 0

for day in range(1, days +1):
    wealth += daily_plunder
    if day % 3 == 0:
        wealth += daily_plunder * 0.5
    if day % 5 == 0:
        wealth -= wealth * 0.3

percentage = (wealth * 100) / expected_plunder
if wealth >= expected_plunder:
    print(f"Ahoy! {wealth:.2f} plunder gained.")
else:
    print(f"Collected only {percentage:.2f}% of the plunder.")